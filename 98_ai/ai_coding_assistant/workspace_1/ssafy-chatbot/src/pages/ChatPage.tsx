
import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { RootState } from '../store/store';
import { addMessage } from '../store/slices/chatSlice';
import { setLoading, setError } from '../store/slices/uiSlice';
import { sendMessage } from '../api/openai';
import './ChatPage.css';

const ChatPage: React.FC = () => {
  const dispatch = useDispatch();
  const { messages } = useSelector((state: RootState) => state.chat);
  const { isLoading } = useSelector((state: RootState) => state.ui);
  const [input, setInput] = useState('');
  const [image, setImage] = useState<string | null>(null);

  const handleSend = async () => {
    const trimmedInput = input.trim();
    if (trimmedInput || image) {
      const userMessage = {
        id: Date.now().toString(),
        text: trimmedInput,
        sender: 'user' as const,
        imageUrl: image || undefined,
      };
      dispatch(addMessage(userMessage));
      setInput('');
      setImage(null);

      dispatch(setLoading(true));
      try {
        const aiResponse = await sendMessage(trimmedInput, image || undefined);
        dispatch(
          addMessage({
            id: (Date.now() + 1).toString(),
            text: aiResponse,
            sender: 'ai' as const,
          })
        );
      } catch (error) {
        dispatch(setError('Failed to get response from AI.'));
      } finally {
        dispatch(setLoading(false));
      }
    }
  };

  const handleImageUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      const reader = new FileReader();
      reader.onload = (event) => {
        setImage(event.target?.result as string);
      };
      reader.readAsDataURL(e.target.files[0]);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-messages">
        {messages.map((msg) => (
          <div key={msg.id} className={`message ${msg.sender}`}>
            <div className="message-content">
              {msg.imageUrl && <img src={msg.imageUrl} alt="upload-preview" className="img-fluid mb-2" />}
              <p>{msg.text}</p>
            </div>
          </div>
        ))}
        {isLoading && (
            <div className="message ai">
                <div className="message-content">
                    <p><i>AI가 응답을 생성하고 있습니다...</i></p>
                </div>
            </div>
        )}
      </div>
      <div className="chat-input-bar">
        {image && (
          <div className="image-preview-container">
            <img src={image} alt="preview" className="image-preview" />
            <button onClick={() => setImage(null)} className="btn-close"></button>
          </div>
        )}
        <div className="input-group">
            <label htmlFor="file-upload" className="btn btn-secondary">
                이미지
            </label>
            <input id="file-upload" type="file" accept="image/*" onChange={handleImageUpload} style={{display: 'none'}}/>
          <input
            type="text"
            className="form-control"
            placeholder="메시지를 입력하세요..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSend()}
            disabled={isLoading}
          />
          <button className="btn btn-primary" onClick={handleSend} disabled={isLoading} style={{ backgroundColor: '#00EEFF', borderColor: '#00EEFF' }}>
            {isLoading ? '전송중...' : '전송'}
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatPage;
