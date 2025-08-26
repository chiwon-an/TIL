import React from 'react';

const SignupPage: React.FC = () => {
  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-6">
          <div className="card">
            <div className="card-body">
              <h1 className="card-title text-center">회원가입</h1>
              <form>
                <div className="mb-3">
                  <label htmlFor="email" className="form-label">이메일 주소</label>
                  <input type="email" className="form-control" id="email" />
                </div>
                <div className="mb-3">
                  <label htmlFor="password" className="form-label">비밀번호</label>
                  <input type="password" className="form-control" id="password" />
                </div>
                <div className="mb-3">
                  <label htmlFor="confirmPassword" className="form-label">비밀번호 확인</label>
                  <input type="password" className="form-control" id="confirmPassword" />
                </div>
                <div className="d-grid">
                  <button type="submit" className="btn btn-primary" style={{ backgroundColor: '#00EEFF', borderColor: '#00EEFF' }}>
                    회원가입
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SignupPage;