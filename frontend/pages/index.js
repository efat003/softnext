import { useState } from 'react'

export default function Home() {
  const [isChatOpen, setIsChatOpen] = useState(false)
  const [messages, setMessages] = useState([
    { text: "Hi! I'm here to help with your website needs.", sender: "bot" }
  ])
  const [inputMessage, setInputMessage] = useState("")

  const sendMessage = () => {
    if (inputMessage.trim()) {
      setMessages([...messages, { text: inputMessage, sender: "user" }])
      setInputMessage("")
      setTimeout(() => {
        setMessages(prev => [...prev, { 
          text: "Thanks for your message! We'll help you shortly.", 
          sender: "bot" 
        }])
      }, 1000)
    }
  }

  return (
    <div style={{ 
      padding: '20px', 
      fontFamily: 'Arial',
      maxWidth: '1200px',
      margin: '0 auto',
      background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      minHeight: '100vh',
      color: 'white'
    }}>
      <header style={{ textAlign: 'center', padding: '40px 0' }}>
        <h1 style={{ fontSize: '3rem', margin: '0' }}>🚀 SoftNext</h1>
        <p style={{ fontSize: '1.2rem', opacity: '0.9' }}>
          Professional Website Templates Marketplace
        </p>
      </header>

      <div style={{ 
        background: 'rgba(255,255,255,0.1)', 
        padding: '30px', 
        borderRadius: '15px',
        backdropFilter: 'blur(10px)'
      }}>
        <h2>🌟 Featured Templates</h2>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '20px', marginTop: '20px' }}>
          {['E-commerce', 'Portfolio', 'Business', 'Blog'].map((type) => (
            <div key={type} style={{
              background: 'rgba(255,255,255,0.2)',
              padding: '20px',
              borderRadius: '10px',
              textAlign: 'center'
            }}>
              <h3>{type} Website</h3>
              <p>Starting at </p>
              <button style={{
                background: '#ff6b6b',
                color: 'white',
                border: 'none',
                padding: '10px 20px',
                borderRadius: '5px',
                cursor: 'pointer'
              }}>
                View Demo
              </button>
            </div>
          ))}
        </div>
      </div>

      <button 
        onClick={() => setIsChatOpen(!isChatOpen)}
        style={{
          position: 'fixed',
          bottom: '20px',
          right: '20px',
          background: '#0070f3',
          color: 'white',
          border: 'none',
          padding: '15px 20px',
          borderRadius: '50px',
          cursor: 'pointer',
          boxShadow: '0 5px 15px rgba(0,0,0,0.3)',
          display: 'flex',
          alignItems: 'center',
          gap: '8px'
        }}
      >
        💬 Live Chat
      </button>

      {isChatOpen && (
        <div style={{
          position: 'fixed',
          bottom: '80px',
          right: '20px',
          width: '350px',
          height: '400px',
          background: 'white',
          border: '1px solid #ccc',
          borderRadius: '10px',
          boxShadow: '0 5px 25px rgba(0,0,0,0.2)',
          display: 'flex',
          flexDirection: 'column',
          color: 'black'
        }}>
          <div style={{
            background: '#0070f3',
            color: 'white',
            padding: '15px',
            borderRadius: '10px 10px 0 0',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center'
          }}>
            <h4 style={{ margin: 0 }}>SoftNext Support</h4>
            <button 
              onClick={() => setIsChatOpen(false)}
              style={{
                background: 'none',
                border: 'none',
                color: 'white',
                cursor: 'pointer'
              }}
            >
              ✕
            </button>
          </div>

          <div style={{
            flex: 1,
            padding: '15px',
            overflowY: 'auto'
          }}>
            {messages.map((msg, index) => (
              <div key={index} style={{
                textAlign: msg.sender === 'user' ? 'right' : 'left',
                marginBottom: '10px'
              }}>
                <div style={{
                  display: 'inline-block',
                  background: msg.sender === 'user' ? '#0070f3' : '#f1f1f1',
                  color: msg.sender === 'user' ? 'white' : 'black',
                  padding: '10px 15px',
                  borderRadius: '15px',
                  maxWidth: '80%'
                }}>
                  {msg.text}
                </div>
              </div>
            ))}
          </div>

          <div style={{
            padding: '15px',
            borderTop: '1px solid #eee',
            display: 'flex',
            gap: '10px'
          }}>
            <input 
              type="text"
              value={inputMessage}
              onChange={(e) => setInputMessage(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
              placeholder="Type your message..."
              style={{
                flex: 1,
                padding: '10px',
                border: '1px solid #ddd',
                borderRadius: '5px'
              }}
            />
            <button 
              onClick={sendMessage}
              style={{
                background: '#0070f3',
                color: 'white',
                border: 'none',
                padding: '10px 15px',
                borderRadius: '5px',
                cursor: 'pointer'
              }}
            >
              Send
            </button>
          </div>
        </div>
      )}
    </div>
  )
}
