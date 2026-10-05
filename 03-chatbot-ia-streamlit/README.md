[← Voltar para todos os projetos](../README.md)

# 💬 ChatBot com IA usando Python e Streamlit

Projeto desenvolvido durante o curso **Python Impressionador (Intensivão de Python)** da **Hashtag Treinamentos**.

Aplicação web de chatbot com Inteligência Artificial, criada com **Streamlit** e integrada ao modelo **Gemini** do Google. O chat mantém o histórico da conversa, permitindo que a IA responda levando em conta as mensagens anteriores.

## 📋 Funcionalidades

- Interface de chat simples e interativa
- Envio de mensagens e resposta da IA em tempo real
- **Memória da conversa:** o histórico é guardado durante a sessão e enviado ao modelo a cada nova mensagem
- Exibição de todo o histórico de mensagens na tela

## 🛠️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [Streamlit](https://streamlit.io/): criação da interface web
- [OpenAI SDK](https://github.com/openai/openai-python): biblioteca para comunicação com a API
- [Google Gemini API](https://ai.google.dev/): modelo de IA (`gemini-flash-lite-latest`), acessado por meio da compatibilidade com o formato da OpenAI

## ⚙️ Como executar

1. Clone o repositório e entre na pasta do projeto:
   ```bash
   git clone https://github.com/seu-usuario/projetos-python-hashtag.git
   cd projetos-python-hashtag/03-chatbot-ia-streamlit
   ```

2. Instale as dependências:
   ```bash
   pip install streamlit openai
   ```

3. Gere uma chave de API gratuita no [Google AI Studio](https://aistudio.google.com/apikey).

4. Copie o arquivo `.streamlit/secrets.toml.example` para `.streamlit/secrets.toml` e cole sua chave:
   ```toml
   GEMINI_API_KEY = "sua-chave-aqui"
   ```

5. Execute a aplicação:
   ```bash
   streamlit run main.py
   ```

6. O navegador abrirá automaticamente em `http://localhost:8501`.

> 🔒 **Segurança:** nunca suba sua chave de API para o GitHub. O arquivo `.streamlit/secrets.toml` está listado no `.gitignore`.

## 🧠 Como funciona

1. O Streamlit guarda as mensagens em `st.session_state` (a "memória" da aplicação)
2. Quando o usuário envia uma mensagem, ela é adicionada ao histórico
3. Todo o histórico é enviado ao modelo Gemini pela API
4. A resposta da IA é exibida na tela e também adicionada ao histórico

## 📁 Estrutura do projeto

```
├── main.py                          # Código da aplicação
├── .streamlit/
│   ├── secrets.toml                 # Sua chave da API (NÃO vai ao GitHub)
│   └── secrets.toml.example         # Modelo do arquivo de chave
└── README.md                        # Documentação do projeto
```

## 📚 Aprendizados

- Criação de aplicações web com Python usando Streamlit
- Consumo de APIs de Inteligência Artificial
- Gerenciamento de estado e memória com `st.session_state`
- Estrutura de mensagens com `role` (user / assistant) e `content`
- Boas práticas de segurança com chaves de API

## 🚀 Próximos passos

- Adicionar um prompt de sistema para definir a personalidade do chatbot
- Exibir a resposta da IA em streaming (palavra por palavra)
- Fazer o deploy no Streamlit Community Cloud
