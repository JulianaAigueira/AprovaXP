import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet } from 'react-native';

export default function LoginScreen() {
  // O React guarda o que o aluno digitar aqui:
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

   // Função que roda quando clica no botão:
  const handleLogin = async () => {
    // Esse aviso vai provar que o botão foi clicado!
    console.log("1. Botão clicado! Tentando chamar o Python no IP 192.168.0.157...");

    try {
      const resposta = await fetch(`http://192.168.0.157:8000/api/token/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: username,
          password: password,
        }),
      });

      const dados = await resposta.json();

      if (resposta.ok) {
        // Se a senha estiver certa, ele entra aqui!
        console.log("SUCESSO! Sua pulseira VIP:", dados.access);
        alert("Login aprovado! Bem-vindo ao AprovaXP! 🎉");
      } else {
        // Se errar a senha ou o usuário, ele entra aqui:
        console.log("ERRO NO LOGIN:", dados);
        alert("Acesso Negado: Usuário ou senha incorretos.");
      }
    } catch (error) {
      // Se o Wi-Fi cair ou o Python estiver desligado:
      console.log("FALHA DE CONEXÃO:", error);
      alert("Não foi possível encontrar o servidor do jogo.");
    }
  };

  return (
    <View style={styles.container}>
      {/* Título do Aplicativo */}
      <Text style={styles.title}>AprovaXP</Text>
      <Text style={styles.subtitle}>Faça login para começar a jogar</Text>

      {/* Campo de Usuário */}
      <TextInput
        style={styles.input}
        placeholder="Nome de usuário (ex: carlos_gamer)"
        value={username}
        onChangeText={setUsername}
        autoCapitalize="none" // Para não colocar letra maiúscula sozinho
      />

      {/* Campo de Senha */}
      <TextInput
        style={styles.input}
        placeholder="Sua senha secreta"
        value={password}
        onChangeText={setPassword}
        secureTextEntry={true} // Esconde a senha com "bolinhas"
      />

      {/* Botão de Entrar */}
      <TouchableOpacity style={styles.button} onPress={handleLogin}>
        <Text style={styles.buttonText}>ENTRAR</Text>
      </TouchableOpacity>
    </View>
  );
}

// A "Maquiagem" do aplicativo:
const styles = StyleSheet.create({
  container: {
    flex: 1, // Ocupa a tela inteira
    justifyContent: 'center', // Centraliza no meio (vertical)
    alignItems: 'center', // Centraliza no meio (horizontal)
    backgroundColor: '#f4f4f9', // Cor de fundo cinza bem clarinho
    padding: 20,
  },
  title: {
    fontSize: 40,
    fontWeight: 'bold',
    color: '#2c3e50', // Azul escuro
    marginBottom: 5,
  },
  subtitle: {
    fontSize: 16,
    color: '#7f8c8d',
    marginBottom: 40,
  },
  input: {
    width: '100%',
    backgroundColor: '#ffffff',
    padding: 15,
    borderRadius: 10,
    marginBottom: 15,
    borderWidth: 1,
    borderColor: '#dcdde1',
    fontSize: 16,
  },
  button: {
    width: '100%',
    backgroundColor: '#3498db', // Azul bonito
    padding: 15,
    borderRadius: 10,
    alignItems: 'center',
    marginTop: 10,
  },
  buttonText: {
    color: '#ffffff',
    fontWeight: 'bold',
    fontSize: 18,
  },
});