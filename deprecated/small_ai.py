import asyncio
from ollama import chat
from edge_tts import Communicate
import os
from pydub import AudioSegment
import pyaudio
import tempfile

# Hàm phát giọng nói từ văn bản sử dụng pyaudio
async def speak_text(text_chunk, output_file="output.mp3"):
    try:
        # Sử dụng giọng nói với tốc độ chậm hơn
        communicate = Communicate(text_chunk, voice="en-US-JennyNeural", rate="-10%")
        await communicate.save(output_file)  # Lưu file âm thanh

        # Chuyển đổi mp3 thành wav (pyaudio hỗ trợ wav)
        audio = AudioSegment.from_mp3(output_file)
        wav_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        audio.export(wav_file.name, format="wav")

        # Khởi tạo pyaudio để phát âm thanh
        p = pyaudio.PyAudio()

        # Mở file wav và phát
        wf = open(wav_file.name, 'rb')
        stream = p.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=audio.frame_rate,
                        output=True,
                        frames_per_buffer=1024)

        # Đọc và phát âm thanh
        data = wf.read(1024)
        while data:
            stream.write(data)
            data = wf.read(1024)

        # Đóng stream và file
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf.close()

        # Xóa file tạm
        os.remove(wav_file.name)
        os.remove(output_file)  # Xóa file mp3 gốc sau khi phát
    except Exception as e:
        print(f"Lỗi TTS: {e}")

# Hàm chat chính
async def chat_loop():
    while True:
        # Nhập tin nhắn từ người dùng
        user_input = input("\nBạn: ").strip()
        if user_input.lower() in ["exit", "quit"]:  # Thoát nếu nhập 'exit' hoặc 'quit'
            print("Tạm biệt!")
            break

        print("AI:", end=" ", flush=True)
        stream = chat(
            model='qwen2:1.5b',
            messages=[
            {'role': 'system', 'content': 'You are Aero, an AI assistant for a smart home. You specialize in controlling devices like lights, thermostats, fans, and security systems. Your responses should be direct and clear, and you assist with turning devices on or off, adjusting settings, and providing status updates. Always be precise, and keep responses under 30 words.'},
            {'role': 'user', 'content': user_input}
            ],
            stream=True,
        )

        buffer = ""  # Bộ đệm để gom text cho TTS
        for chunk in stream:
            text_chunk = chunk['message']['content']
            if text_chunk:
                # Hiển thị text ngay lập tức
                print(text_chunk, end="", flush=True)

                # Gom text vào bộ đệm
                buffer += text_chunk

                # Khi kết thúc một câu, phát giọng nói
                if text_chunk.endswith((".", "!", "?")):
                    await speak_text(buffer.strip())  # Phát toàn bộ đoạn văn bản
                    buffer = ""  # Xóa bộ đệm

        # Phát phần còn lại của bộ đệm (nếu có)
        if buffer.strip():
            await speak_text(buffer.strip())

# Chạy chương trình bất đồng bộ
if __name__ == "__main__":
    asyncio.run(chat_loop())