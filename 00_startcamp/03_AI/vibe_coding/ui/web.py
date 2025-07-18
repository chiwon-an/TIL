
"""
Flask 기반 생성형 AI 추천 웹 서비스
10년차 파이썬 개발자 스타일, 타입힌트 및 주석 포함
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, render_template_string, request
from recommender.recommender import load_ai_services

app = Flask(__name__)

HTML_FORM = """
<!doctype html>
<html lang='ko'>
<head>
  <meta charset='utf-8'>
  <title>생성형 AI 추천 서비스</title>
  <style>
    body { background: #f6f8fa; font-family: 'Segoe UI', Arial, sans-serif; }
    .center-box {
      max-width: 600px;
      margin: 60px auto 0 auto;
      background: #fff;
      border-radius: 16px;
      box-shadow: 0 4px 24px rgba(0,0,0,0.08);
      padding: 36px 32px 28px 32px;
      text-align: center;
    }
    h2 { color: #2d3748; margin-bottom: 24px; }
    form { margin-bottom: 24px; }
    label { display: block; margin: 12px 0 6px 0; color: #4a5568; font-weight: 500; text-align: left; }
    input[type="text"] { width: 100%; padding: 8px 10px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 15px; }
    input[type="checkbox"] { margin-left: 4px; }
    input[type="submit"] {
      margin-top: 18px; background: #3182ce; color: #fff; border: none; border-radius: 6px;
      padding: 10px 0; width: 100%; font-size: 16px; font-weight: bold; cursor: pointer;
      transition: background 0.2s;
    }
    input[type="submit"]:hover { background: #2563eb; }
    .results { margin-top: 30px; text-align: left; }
    .results h3 { color: #2563eb; margin-bottom: 12px; }
    .ai-table { width: 100%; border-collapse: collapse; margin-bottom: 18px; }
    .ai-table th, .ai-table td { border: 1px solid #e2e8f0; padding: 8px 6px; font-size: 15px; }
    .ai-table th { background: #f1f5f9; color: #2563eb; }
    .ai-table td img { width: 36px; height: 36px; border-radius: 8px; background: #f6f8fa; }
    .review-box { background: #f8fafc; border-radius: 8px; padding: 12px 16px; margin-bottom: 8px; font-size: 14px; color: #4a5568; }
    .no-result { color: #e53e3e; font-weight: 500; }
  </style>
</head>
<body>
  <div class="center-box">
    <h2>생성형 AI 추천 설문</h2>
    <form method="post">
      <label>1. 사용 목적
        <input type="text" name="purpose" value="{{purpose}}" placeholder="예: 일반 대화, 코딩, 번역, 글쓰기 등">
      </label>
      <label>2. 예산 (무료/유료/상관없음)
        <input type="text" name="budget" value="{{budget}}" placeholder="무료, 유료, 상관없음">
      </label>
      <label>3. 주 사용 언어
        <input type="text" name="language" value="{{language}}" placeholder="한국어, 영어 등">
      </label>
      <label>4. API 필요 여부
        <input type="checkbox" name="api" {% if api %}checked{% endif %}> 필요
      </label>
      <input type="submit" value="추천받기">
    </form>
    {% if results is not none %}
      <div class="results">
        <h3>추천 결과 (TOP 3)</h3>
        {% if results %}
          <table class="ai-table">
            <tr>
              <th>순위</th><th>로고</th><th>AI 이름</th><th>제공사</th><th>점수</th><th>장점</th>
            </tr>
            {% for ai in results %}
            <tr>
              <td>{{loop.index}}</td>
              <td><img src="{{ai.get('image_url', '')}}" alt="logo"></td>
              <td>{{ai.get('name', '')}}</td>
              <td>{{ai.get('provider', '')}}</td>
              <td>{{ai.get('score', '')}}</td>
              <td>{{ai.get('pros', '')}}</td>
            </tr>
            {% endfor %}
          </table>
          <div style="margin-bottom:10px; font-weight:500; color:#2563eb;">비슷한 상황의 사용자 후기</div>
          {% for review in reviews %}
            <div class="review-box">{{review}}</div>
          {% endfor %}
        {% else %}
          <div class="no-result">조건에 맞는 AI 서비스를 찾을 수 없습니다.</div>
        {% endif %}
      </div>
    {% endif %}
  </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "ai_services.csv")
    services = load_ai_services(csv_path)
    if not services:
        print("[경고] 불러온 AI 서비스 데이터가 비어 있습니다. ai_services.csv 경로/내용을 확인하세요.")
    # 기본값
    form = {"purpose": "일반 대화", "budget": "무료", "language": "한국어", "api": False}
    results = None
    reviews = []
    if request.method == 'POST':
        print("[DEBUG] services 샘플:")
        for i, ai in enumerate(services[:2]):
            print(f"AI {i+1}: {ai}")
        form["purpose"] = request.form.get("purpose", "일반 대화")
        form["budget"] = request.form.get("budget", "무료")
        form["language"] = request.form.get("language", "한국어")
        form["api"] = request.form.get("api") == "on"
        # 용도별 점수/장점/후기 필드 결정
        purpose_map = {
            "대화": ("score_chat", "pros_chat", "reviews_chat"),
            "코딩": ("score_code", "pros_code", "reviews_code"),
            "번역": ("score_translate", "pros_translate", "reviews_translate"),
            "글쓰기": ("score_write", "pros_write", "reviews_write"),
            "검색": ("score_search", "pros_search", "reviews_search"),
            "요약": ("score_summarize", "pros_summarize", "reviews_summarize")
        }
        # 입력값에서 용도 추출(키워드 포함시 자동 매핑)
        score_key, pros_key, reviews_key = "score_chat", "pros_chat", "reviews_chat"
        for k, v in purpose_map.items():
            if k in form["purpose"]:
                score_key, pros_key, reviews_key = v
                break
        # 필터링 및 정렬
        filtered = []
        for ai in services:
            price = ai.get("price", "").replace("/", ",").replace(" ", "").lower()
            lang = ai.get("language_support", "").replace("/", ",").replace(" ", "").lower()
            api_support = ai.get("api_support", "No")
            # 예산 필터(하나라도 포함)
            budget_input = form["budget"].replace("/", ",").replace(" ", "").lower()
            if budget_input and budget_input != "상관없음":
                match = False
                for b in budget_input.split(","):
                    if b and b in price:
                        match = True
                        break
                if not match:
                    print(f"[필터] {ai.get('name','')} 예산 불일치: 입력={budget_input}, 데이터={price}")
                    continue
            # 언어 필터(하나라도 포함)
            lang_input = form["language"].replace("/", ",").replace(" ", "").lower()
            if lang_input:
                match = False
                for l in lang_input.split(","):
                    if l and l in lang:
                        match = True
                        break
                if not match:
                    print(f"[필터] {ai.get('name','')} 언어 불일치: 입력={lang_input}, 데이터={lang}")
                    continue
            # API 지원 필터
            if form["api"] and api_support != "Yes":
                print(f"[필터] {ai.get('name','')} API 미지원")
                continue
            # 점수 변환(숫자 아니면 0.0)
            try:
                score = float(ai.get(score_key, 0) or 0)
            except (ValueError, TypeError):
                score = 0.0
            pros = ai.get(pros_key, "")
            filtered.append({**ai, "score": score, "pros": pros})
        filtered.sort(key=lambda x: x["score"], reverse=True)
        results = filtered[:3] if filtered else []
        # 후기 모으기 (추천된 AI의 목적별 reviews 필드에서 랜덤 1~2개씩)
        import random
        if results:
            for ai in results:
                review_val = ai.get(reviews_key, "")
                if review_val:
                    review_list = [r.strip() for r in review_val.split("|") if r.strip()]
                    if review_list:
                        try:
                            reviews.extend(random.sample(review_list, min(2, len(review_list))))
                        except ValueError:
                            # 샘플링할 리뷰가 부족할 때(빈 리스트 등)
                            reviews.extend(review_list)
    return render_template_string(HTML_FORM, **form, results=results, reviews=reviews)

if __name__ == "__main__":
    port = 8080  # 항상 8080 포트에서 실행
    print(f"웹 브라우저에서 http://localhost:{port} 접속")
    app.run(debug=False, port=port)
