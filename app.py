import streamlit as st

# Título do aplicativo
st.title("Dry Eye Discover")
st.write("Este aplicativo consulta a tabela 'participantes' do banco de dados PostgresSQL.")

# Conectar ao banco de dados usando st.connection
conn = st.connection("postgres", type="sql")

# Executar a query e armazenar o resultado em um DataFrame
df = conn.query(
    'SELECT participante.genero, AVG(questionario.qualidade_sono) AS media '
    'FROM participante '
    'INNER JOIN questionario ON participante.id_participante = questionario.id_participante_id '
    'GROUP BY participante.genero;'
)

# Exibir o DataFrame
st.write("### Média de qualidade de sono por gênero:")
st.dataframe(df)

# Exibir gráfico de barras
st.write("### Gráfico de exemplo:")
st.bar_chart(df, x='genero', y='media')
