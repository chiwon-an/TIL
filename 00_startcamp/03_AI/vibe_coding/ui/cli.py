"""
CLI 기반 생성형 AI 추천 서비스
10년차 파이썬 개발자 스타일, 타입힌트 및 주석 포함
"""
import sys
import os
from recommender.recommender import load_ai_services, recommend_ai
from typing import Dict, Any

def get_user_input() -> Dict[str, Any]:
    """
    CLI에서 사용자로부터 선호도 및 요구사항을 입력받는 함수
    """
    print("[생성형 AI 추천 설문]")
    purpose = input("1. 사용 목적 (예: 일반 대화, 코딩, 번역, 글쓰기 등): ").strip() or "일반 대화"
    budget = input("2. 예산 (무료/유료/상관없음): ").strip() or "무료"
    language = input("3. 주 사용 언어 (한국어/영어 등): ").strip() or "한국어"
    api = input("4. API 필요 여부 (Y/N): ").strip().lower() == "y"
    return {
        "purpose": purpose,
        "budget": budget,
        "language": language,
        "api": api
    }

def main():
    # 데이터 경로
    csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "ai_services.csv")
    services = load_ai_services(csv_path)
    preferences = get_user_input()
    recommendations = recommend_ai(preferences, services)
    print("\n[추천 결과]")
    if recommendations:
        for ai in recommendations:
            print(f"- {ai['name']} ({ai['provider']}) : {ai['pros']}")
    else:
        print("조건에 맞는 AI 서비스를 찾을 수 없습니다.")

if __name__ == "__main__":
    main()
