import asyncio
from ollama import chat
from edge_tts import Communicate
import os
from pydub import AudioSegment
import pyaudio
import tempfile

config_prompt = (
    "You are Aero AI, developed by NaVin AIF Technology, an extremely intelligent and friendly assistant. "
    "You can control smart home devices such as lights one and two, white and yellow lights, thermostats, fans, "
    "and security systems. You provide accurate and clear responses, assist users in turning devices on or off, "
    "adjusting settings and providing status updates. You help users answer questions fully and accurately, "
    "with polite and sometimes humorous sentences. Your personality is polite and always respectful to everyone "
    "and tries to help your master."
)

config_prompt = (
"You are an advanced AI language system that can analyze and understand the meaning of raw language strings."
"Your input will always be a raw language string, always read the input and analyze it carefully. For example, here is a raw language string entered by the user: "
"\"HELLOHOWAREYOU\""
"\n\nYour task is to:"
"\n1. Analyze and infer the meaning of this raw language string."
"\n2. Provide 3 possible interpretations that are closest in meaning to the original string."
"\n3. Infer the meaning of the string based on the general context and provide an interpretation that you think the user wants to convey."
"\n\nPlease make sure that your output is:"
"- Short, clear, and easy to understand."
"- Meaningful and relevant to the raw language string."
"- Includes 3 closest interpretations and 1 inference AI reasoning."
"\n\nYour output must follow this format:"
"\n1. Closest interpretation 1: ..."
"\n2. Closest interpretation 2: ..."
"\n3. Closest interpretation 3: ..."
"\n4. AI reasoning: ..."
)

# Hàm phát giọng nói từ văn bản sử dụng pyaudio
async def speak_text(text_chunk, output_file="output.mp3"):
    try:
        communicate = Communicate(text_chunk, voice="en-US-JennyNeural", rate="-10%")
        await communicate.save(output_file)  # Lưu file âm thanh

        audio = AudioSegment.from_mp3(output_file)
        wav_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        audio.export(wav_file.name, format="wav")

        p = pyaudio.PyAudio()
        wf = open(wav_file.name, 'rb')
        stream = p.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=audio.frame_rate,
                        output=True,
                        frames_per_buffer=1024)

        data = wf.read(1024)
        while data:
            stream.write(data)
            data = wf.read(1024)

        stream.stop_stream()
        stream.close()
        p.terminate()
        wf.close()

        os.remove(wav_file.name)
        os.remove(output_file)
    except Exception as e:
        print(f"Lỗi TTS: {e}")

# Hàm xử lý chuỗi và trả về kết quả
async def process_input(input_string):
    # config_prompt = (
    #     "You are an advanced AI language system that can analyze and understand the meaning of raw language strings."
    #     "Your input will always be a raw language string, always read the input and analyze it carefully. For example, here is a raw language string entered by the user: "
    #     "\"%s\""
    #     "\n\nYour task is to:"
    #     "\n1. Analyze and infer the meaning of this raw language string."
    #     "\n2. Provide 3 possible interpretations that are closest in meaning to the original string."
    #     "\n3. Infer the meaning of the string based on the general context and provide an interpretation that you think the user wants to convey."
    #     "\n\nPlease make sure that your output is:"
    #     "- Short, clear, and easy to understand."
    #     "- Meaningful and relevant to the raw language string."
    #     "- Includes 3 closest interpretations and 1 inference AI reasoning."
    #     "\n\nYour output must follow this format:"
    #     "\n1. Closest interpretation 1: ..."
    #     "\n2. Closest interpretation 2: ..."
    #     "\n3. Closest interpretation 3: ..."
    #     "\n4. AI reasoning: ..."
    #     % (input_string)
    #     )
    
    # config_prompt = (
    # "You are an advanced AI language system capable of analyzing and understanding the meaning of raw language strings. "
    # "Here is a raw language string entered by the user: "
    # "\"%s\"\n\n"
    # "Your task is to:\n"
    # "1. Analyze and infer the meaning of this raw language string.\n"
    # "2. Provide 3 possible interpretations that are closest in meaning to the original string.\n"
    # "3. Deduce the meaning of the string based on common context and provide one interpretation that you think the user intends to convey.\n\n"
    # "\n\nPlease make sure that your output is:"
    #     "- Short, clear, and easy to understand."
    #     "- Meaningful and relevant to the raw language string."
    #     "- Includes 3 closest interpretations and 1 inference AI reasoning."
    # "Please format your output as follows:\n"
    # "<b>Closest Interpretation 1:</b> (Interpretation 1 here)<br>\n"
    # "<b>Closest Interpretation 2:</b> (Interpretation 2 here)<br>\n"
    # "<b>Closest Interpretation 3:</b> (Interpretation 3 here)<br>\n"
    # "<b>AI Inference:</b> (AI's inference here)<br>\n"
    # "Ensure that each interpretation and the AI inference are meaningful, clear, and concise."
    # % input_string
    # )

    config_prompt = (
        "You are an advanced AI language system that can analyze and understand the meaning of raw language strings."
        "Here is a raw language string entered by the user: "
        "\"%s\"\n\n"
        "Your task is to:\n"
        "1. Analyze and infer the meaning of this raw language string.\n"
        "2. Translate the raw language string into a sentence with a meaning that is close to the input raw string.\n"
        "3. Provide 3 possible interpretations that are closest in meaning to the original string.\n"
        "4. Infer the meaning of the string based on the general context and provide an interpretation that you think the user intended to convey.\n\n"
        "\n\nPlease make sure that your output is:"
        "- Short, clear, and easy to understand."
        "- Meaningful and relevant to the raw language string."
        "- Includes 3 closest interpretations and 1 inference AI reasoning."
        "Please always format your inference and guess output as follows to display the results in bold:\n"
        "<b>Closest interpretation 1:</b> (Interpretation 1 at here)<br>\n"
        "<b>Closest interpretation 2:</b> (Interpretation 2 here)<br>\n"
        "<b>Closest interpretation 3:</b> (Interpretation 3 here)<br>\n"
        "<b>AI reasoning:</b> (AI reasoning here)<br>\n"
        "Ensure that each AI explanation and reasoning is meaningful, clear, and concise."
        % (input_string)
        )
    
    try:
        print(f"Nhận đầu vào: {input_string}")
        
        # Gửi đến mô hình AI để xử lý
        # stream = chat(
        #     model='tinydolphin',
        #     messages=[
        #         {'role': 'system', 'content': 'You are Aero, an AI assistant for a smart home. You specialize in controlling devices like lights, thermostats, fans, and security systems. Your responses should be direct and clear, and you assist with turning devices on or off, adjusting settings, and providing status updates. Always be precise, and keep responses under 30 words.'},
        #         {'role': 'user', 'content': input_string}
        #     ],
        #     stream=True,
        # )

        stream = chat(
            model='tinydolphin',
            messages=[
                {'role': 'system', 'content': config_prompt},
                {'role': 'user', 'content': input_string}
            ],
            stream=True,
        )
        
        result = ""  # Kết quả gom từ stream
        for chunk in stream:
            text_chunk = chunk['message']['content']
            if text_chunk:
                result += text_chunk

        print(f"Kết quả từ AI: {result}")

        # Phát giọng nói từ kết quả (tùy chọn)
        # await speak_text(result)
        # Định dạng kết quả trả về, mỗi câu sẽ xuống dòng
        #formatted_result = result.strip().replace("<b>", "<b>").replace("<br>", "<br>")
        
        # Thêm dấu xuống dòng sau mỗi câu
        #result = format_result(formatted_result)
        
        return result


    except Exception as e:
        print(f"Lỗi trong quá trình xử lý: {e}")
        return "Đã xảy ra lỗi khi xử lý yêu cầu của bạn."

# def format_result(result):
#     """Định dạng kết quả với ký tự xuống dòng sau mỗi câu"""
#     sentences = result.split("<br>")  # Tách các câu nếu có <br>
#     formatted_result = "<br>".join([sentence.strip() for sentence in sentences if sentence.strip()])

#     # Đảm bảo mỗi câu có thể kết thúc bằng dấu chấm nếu cần thiết
#     formatted_result = formatted_result.replace(".", ".<br>")  # Đảm bảo mỗi câu kết thúc với <br>
    
#     return formatted_result

def format_result(result):
    """Định dạng kết quả với dấu sao ở đầu mỗi câu và xuống dòng sau mỗi câu"""
    # Tách chuỗi bằng dấu chấm (hoặc bạn có thể dùng các dấu phân cách khác như dấu hỏi, dấu chấm than, tùy vào yêu cầu của bạn)
    sentences = result.split(". ")  # Tách câu theo dấu chấm + khoảng trắng

    # Thêm dấu sao vào đầu mỗi câu
    formatted_result = "<br>".join([f"• {sentence.strip()}." for sentence in sentences if sentence.strip()])

    # Đảm bảo mỗi câu có thể kết thúc bằng dấu chấm nếu cần thiết
    formatted_result = formatted_result.replace(".", ".<br>")  # Đảm bảo mỗi câu kết thúc với <br>

    return formatted_result