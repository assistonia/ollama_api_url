import requests
import json

OLLAMA_API_URL = "http://0.0.0.0:11434/api/generate"  # 로컬 URL 사용  다른 컴퓨터에서 사용할시 컴퓨터 포트 열고 아이피 맞추기
#OLLAMA 0.0.0.0으로 변경해야가능
MODEL_NAME = "llama3.1:latest"  # 사용할 모델 활용

def query_ollama(prompt):
    """Ollama API에 요청을 보내고 응답을 받는 함수"""
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False  # True로 하면 스트리밍 응답 가능
    }
    headers = {
        "Content-Type": "application/json",
        "ngrok-skip-browser-warning": "true"  # ngrok 브라우저 경고 무시
    }

    response = requests.post(OLLAMA_API_URL, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return f"Error: {response.status_code}, {response.text}"

# 테스트 실행
if __name__ == "__main__":
    prompt_text = "Hello, how are you? what are you think about bitcoin?"
    response_text = query_ollama(prompt_text)
    print("Ollama 응답:", response_text)
