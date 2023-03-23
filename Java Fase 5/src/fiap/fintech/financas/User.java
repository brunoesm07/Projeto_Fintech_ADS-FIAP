package fiap.fintech.financas;


public class User {
	int id;
	String nome;
	String email;
	String senha;
	String cpf;
	String telefone;
	
	public User(int id, String nome, String email, String senha, String cpf,String telefone) {
		this.id = id;
		this.nome = nome;
		this.email = email;
		this.senha = senha;
		this.cpf = cpf;
		this.telefone = telefone;
	}
	
	
	public String consultarInformacoes() {
		return "O usuário de nome " + this.nome + ", e seu email é " + this.email ;
	}
	public String consultarCpf() {
		return this.cpf;
	}
	public String consultarTelefone() {
		return this.telefone;
	}


}
