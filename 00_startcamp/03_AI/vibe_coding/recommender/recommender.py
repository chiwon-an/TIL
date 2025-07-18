"""
생성형 AI 추천 로직 (룰베이스)
10년차 파이썬 개발자 스타일, 타입힌트 및 주석 포함
"""
from typing import List, Dict, Any
import csv
import os

# 사용자 입력 설문 항목 정의
def get_user_preferences() -> Dict[str, Any]:
    """
    사용자로부터 선호도 및 요구사항을 입력받는 함수 (예시)
    실제 서비스에서는 CLI/웹 등 UI로 대체
    """
    preferences = {
        "purpose": "일반 대화",  # 예: 일반 대화, 코딩, 번역, 글쓰기 등
        "budget": "무료",        # 예: 무료, 유료 상관없음
        "language": "한국어",   # 예: 한국어, 영어 등
        "api": True             # API 필요 여부
    }
    return preferences

# AI 서비스 데이터 로드 함수
def load_ai_services(csv_path: str) -> List[Dict[str, str]]:
    services = []
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            services.append(row)
    return services

# 간단한 룰베이스 추천 함수
def recommend_ai(preferences: Dict[str, Any], services: List[Dict[str, str]]) -> List[Dict[str, str]]:
    results = []
    for service in services:
        # 예시: 예산, 언어, API 필요 여부만 필터링
        if preferences["budget"] in service["price"] and \
           preferences["language"] in service["language_support"] and \
           (not preferences["api"] or service["api_support"] == "Yes"):
            results.append(service)
    return results

if __name__ == "__main__":
    # 데이터 경로
    csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "ai_services.csv")
    services = load_ai_services(csv_path)
    preferences = get_user_preferences()
    recommendations = recommend_ai(preferences, services)
    print("[추천 결과]")
    for ai in recommendations:
        print(f"- {ai['name']} ({ai['provider']}) : {ai['pros']}")
