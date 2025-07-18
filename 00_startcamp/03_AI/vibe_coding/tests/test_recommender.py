"""
recommender 모듈 테스트 코드
10년차 파이썬 개발자 스타일, 타입힌트 및 주석 포함
"""
import os
import sys
import pytest
from recommender.recommender import load_ai_services, recommend_ai

def get_test_csv_path() -> str:
    return os.path.join(os.path.dirname(__file__), "..", "data", "ai_services.csv")

def test_recommend_free_korean_api():
    services = load_ai_services(get_test_csv_path())
    preferences = {
        "purpose": "일반 대화",
        "budget": "무료",
        "language": "한국어",
        "api": True
    }
    results = recommend_ai(preferences, services)
    assert any(ai["name"] == "ChatGPT" for ai in results)
    assert all("무료" in ai["price"] for ai in results)
    assert all("한국어" in ai["language_support"] for ai in results)
    assert all(ai["api_support"] == "Yes" for ai in results)

def test_recommend_english_noapi():
    services = load_ai_services(get_test_csv_path())
    preferences = {
        "purpose": "코딩",
        "budget": "유료",
        "language": "영어",
        "api": False
    }
    results = recommend_ai(preferences, services)
    assert all("영어" in ai["language_support"] for ai in results)
    assert all("유료" in ai["price"] or "무료" in ai["price"] for ai in results)

if __name__ == "__main__":
    pytest.main([__file__])
