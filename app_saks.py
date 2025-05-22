import streamlit as st
import openai
import os
import pandas as pd

st.set_page_config(page_title="SAKS ONE", layout="centered")

# Configure sua API key da OpenAI
openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

# Estado inicial
if "pagina" not in st.session_state:
    st.session_state.pagina = "home"

# Navegação por sessão
if st.session_state.pagina == "home":
    st.markdown("# SAKS ONE")
    st.markdown("## O centro de comando da inteligência financeira")
    st.text_input("", "Faça uma pergunta ao SAKS ONE", disabled=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("➕ Advisor+", key="menu_advisor"):
            st.session_state.pagina = "advisor"
        st.caption("Negocie com inteligência. Proponha com impacto.")

        if st.button("📘 Vision", key="menu_vision"):
            st.session_state.pagina = "vision"
        st.caption("Relatórios que convencem. Em segundos.")

    with col2:
        if st.button("📊 Insight", key="menu_insight"):
            st.session_state.pagina = "insight"
        st.caption("Cada produto, uma tese. Cada tese, uma oportunidade.")

        if st.button("📡 Radar", key="menu_radar"):
            st.session_state.pagina = "radar"
        st.caption("Exposição sob controle. Risco na palma da mão.")

    with col3:
        if st.button("🛡 Shield", key="menu_shield"):
            st.session_state.pagina = "shield"
        st.caption("Compliance em tempo real, sem fricção.")

        if st.button("💓 Pulse One", key="menu_pulse"):
            st.session_state.pagina = "pulse"
        st.caption("Suporte que antecipa. Respostas que resolvem.")

    st.markdown("---")
    if st.button("🎓 Academy", key="menu_academy"):
        st.session_state.pagina = "academy"
    st.caption("Aprenda como um mestre. Explique como um gênio.")

# Página Advisor+
elif st.session_state.pagina == "advisor":
    st.markdown("# ➕ Advisor+ | IA aplicada ao atendimento internacional")

    if "advisor_chat" not in st.session_state:
        st.session_state.advisor_chat = [
            {"role": "system", "content": "Você é um advisor da SAKS especializado em mercados financeiros internacionais. Sempre responda com foco em produtos, teses, estratégias ou análises relevantes para investimentos globais. Se a pergunta fugir do contexto de investimentos internacionais, informe educadamente que está fora do escopo da SAKS."}
        ]

    for msg in st.session_state.advisor_chat[1:]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Faça sua pergunta sobre investimentos internacionais")
    if user_input:
        st.session_state.advisor_chat.append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Consultando inteligência financeira..."):
                try:
                    response = openai.chat.completions.create(
                        model="o4-mini",
                        messages=st.session_state.advisor_chat
                    )
                    output = response.choices[0].message.content
                    st.markdown(output)
                    st.session_state.advisor_chat.append({"role": "assistant", "content": output})
                except Exception as e:
                    st.error(f"Erro ao consultar a API: {e}")

    if st.button("⬅ Voltar"):
        st.session_state.pagina = "home"
        st.session_state.pagina = "home"

# Página Insight
elif st.session_state.pagina == "insight":
    st.markdown("# 📊 Insight | Análise de Produto e Tese de Investimento")
    st.markdown("Digite abaixo o nome do produto, tese ou dúvida técnica.")

    insight_input = st.text_area("Prompt do usuário (Insight)", "Explique a tese de um CLN com capital garantido atrelado a ações europeias")

    if st.button("🔍 Consultar Insight IA"):
        with st.spinner("Consultando inteligência financeira..."):
            try:
                response = openai.chat.completions.create(
                    model="o4-mini",
                    messages=[
                        {"role": "system", "content": "Você está no módulo INSIGHT da SAKS. Responda com foco em explicação técnica, estrutura de produtos e tese de investimento internacional. Se o usuário pedir uma recomendação, direcione para o módulo Advisor+. Se fugir de investimentos internacionais, diga que está fora do escopo da SAKS."},
                        {"role": "user", "content": insight_input}
                    ]
                )
                insight_output = response.choices[0].message.content
                st.success("Resposta da IA:")
                st.caption(f"🧠 Modelo utilizado: `{response.model}`")
                st.markdown(insight_output)
            except Exception as e:
                st.error(f"Erro ao consultar a API da OpenAI: {e}")

    if st.button("⬅ Voltar"):
        st.session_state.pagina = "home"

# Página Shield
elif st.session_state.pagina == "shield":
    st.markdown("# 🛡 Shield | IA para compliance e validações")
    shield_input = st.text_area("Sua dúvida sobre regras de suitability ou compliance internacional:")
    if st.button("🔍 Consultar Shield IA"):
        with st.spinner("Analisando políticas de compliance..."):
            try:
                response = openai.chat.completions.create(
                    model="o4-mini",
                    messages=[
                        {"role": "system", "content": "Você está no módulo SHIELD da SAKS. Responda com foco em regras internacionais de suitability, perfil de risco e compliance regulatório. Se a pergunta envolver produto ou recomendação, direcione para Advisor+ ou Insight. Se não tiver relação com compliance financeiro internacional, diga que está fora do escopo."},
                        {"role": "user", "content": shield_input}
                    ]
                )
                st.success("Resposta da IA:")
                st.caption(f"🧠 Modelo utilizado: `{response.model}`")
                st.markdown(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Erro ao consultar a API da OpenAI: {e}")
    if st.button("⬅ Voltar"):
        st.session_state.pagina = "home"

# Página Vision
elif st.session_state.pagina == "vision":
    st.markdown("# 📘 Vision")
    st.write("Relatórios prontos e geração de documentos...")
    if st.button("⬅ Voltar"):
        st.session_state.pagina = "home"

# Página Radar
elif st.session_state.pagina == "radar":
    st.markdown("# 📡 Radar | Análise de Risco e Exposição Internacional")
    radar_input = st.text_area("Digite uma pergunta sobre risco ou exposição de clientes internacionais:")
    if st.button("🔍 Consultar Radar IA"):
        with st.spinner("Calculando cenários e risco global..."):
            try:
                response = openai.chat.completions.create(
                    model="o4-mini",
                    messages=[
                        {"role": "system", "content": "Você está no módulo RADAR da SAKS. Foque sua resposta na avaliação de risco, exposição setorial, geográfica ou cambial em investimentos internacionais. Se a pergunta for sobre recomendação, envie para Advisor+. Se fugir do contexto de risco global, informe que está fora do escopo."},
                        {"role": "user", "content": radar_input}
                    ]
                )
                st.success("Resposta da IA:")
                st.caption(f"🧠 Modelo utilizado: `{response.model}`")
                st.markdown(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Erro ao consultar a API da OpenAI: {e}")
    if st.button("⬅ Voltar"):
        st.session_state.pagina = "home"

# Página Pulse One
elif st.session_state.pagina == "pulse":
    st.markdown("# 💓 Pulse One | Central de Atendimento GPT-native")
    pulse_input = st.text_area("Qual a dúvida ou solicitação do cliente?")
    if st.button("🔍 Consultar Pulse IA"):
        with st.spinner("Consultando central de atendimento da SAKS..."):
            try:
                response = openai.chat.completions.create(
                    model="o4-mini",
                    messages=[
                        {"role": "system", "content": "Você está no módulo PULSE ONE da SAKS. Responda como um atendente de alto nível que resolve dúvidas, esclarece prazos e orienta clientes internacionais. Se for sobre produtos, envie para Advisor+. Se fugir de atendimento financeiro internacional, informe que não se aplica."},
                        {"role": "user", "content": pulse_input}
                    ]
                )
                st.success("Resposta da IA:")
                st.caption(f"🧠 Modelo utilizado: `{response.model}`")
                st.markdown(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Erro ao consultar a API da OpenAI: {e}")
    if st.button("⬅ Voltar"):
        st.session_state.pagina = "home"

# Página Academy
elif st.session_state.pagina == "academy":
    st.markdown("# 🎓 Academy | Treinamento em Investimentos Internacionais")
    academy_input = st.text_area("O que você deseja aprender ou simular?")
    if st.button("📘 Consultar Academy IA"):
        with st.spinner("Preparando material educativo e simulações..."):
            try:
                response = openai.chat.completions.create(
                    model="o4-mini",
                    messages=[
                        {"role": "system", "content": "Você está no módulo ACADEMY da SAKS. Ensine conceitos sobre produtos financeiros internacionais, simule pitches e ajude o usuário a aprender sobre finanças globais. Se pedirem recomendação ou avaliação, oriente usar Advisor+ ou Insight. Fora desse contexto, diga que está fora do escopo."},
                        {"role": "user", "content": academy_input}
                    ]
                )
                st.success("Resposta da IA:")
                st.caption(f"🧠 Modelo utilizado: `{response.model}`")
                st.markdown(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Erro ao consultar a API da OpenAI: {e}")
    if st.button("⬅ Voltar"):
        st.session_state.pagina = "home"
