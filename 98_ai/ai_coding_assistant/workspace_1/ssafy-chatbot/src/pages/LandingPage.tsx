import React from 'react';
import { Link } from 'react-router-dom';
import './LandingPage.css';

const LandingPage: React.FC = () => {
  return (
    <div className="landing-container text-center text-white">
      {/* Hero Section */}
      <header className="masthead">
        <div className="container d-flex h-100 align-items-center">
          <div className="mx-auto text-center">
            <h1 className="mx-auto my-0 text-uppercase">SSAFY Chatbot</h1>
            <h2 className="text-white-50 mx-auto mt-2 mb-5">AI 기반 챗봇 서비스로, 당신의 모든 질문에 답해드립니다.</h2>
            <Link to="/chat" className="btn btn-primary" style={{ backgroundColor: '#00EEFF', borderColor: '#00EEFF', color: '#000'}}>
              지금 시작하기
            </Link>
          </div>
        </div>
      </header>

      {/* Features Section */}
      <section className="features-section bg-light text-dark">
        <div className="container px-4 px-lg-5">
          <div className="row gx-4 gx-lg-5">
            <div className="col-md-4 mb-5">
              <div className="card h-100">
                <div className="card-body text-center">
                    <i className="bi-chat-dots fs-1 text-primary" style={{ color: '#00EEFF !important' }}></i>
                    <h4 className="card-title mt-3">AI 채팅</h4>
                    <p className="card-text">GPT-5-nano 모델을 기반으로 한 AI와 자유롭게 대화하세요.</p>
                </div>
              </div>
            </div>
            <div className="col-md-4 mb-5">
                <div className="card h-100">
                    <div className="card-body text-center">
                        <i className="bi-card-image fs-1 text-primary" style={{ color: '#00EEFF !important' }}></i>
                        <h4 className="card-title mt-3">이미지 업로드</h4>
                        <p className="card-text">텍스트와 함께 이미지를 업로드하여 더 풍부한 컨텍스트의 질문을 할 수 있습니다.</p>
                    </div>
                </div>
            </div>
            <div className="col-md-4 mb-5">
                <div className="card h-100">
                    <div className="card-body text-center">
                        <i className="bi-phone fs-1 text-primary" style={{ color: '#00EEFF !important' }}></i>
                        <h4 className="card-title mt-3">반응형 UI</h4>
                        <p className="card-text">모바일, 태블릿, 데스크탑 등 모든 기기에서 최적화된 화면을 제공합니다.</p>
                    </div>
                </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default LandingPage;