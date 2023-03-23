package fiap.fintech.financas;

import java.util.List;

	public class Conta {
		int id;
		double saldo;
		User usuario;
		List<Transacao> transacoes;
		List<Investimento> investimentos;
		boolean ativo;
	
	public Conta( int id,double saldo,User usuario, List<Transacao> transacoes,List<Investimento> investimentos,boolean ativo) {
		this.id = id;
		this.saldo =saldo;
		this.usuario = usuario;
		this.transacoes = transacoes;
		this.investimentos = investimentos;
		this.ativo = ativo;
	}
	public int consultarId() {
		return this.id;
	}
	public double consultarSaldo() {
		return this.saldo;
	}
	public User consultarUsuario() {
		return this.usuario;
	}
	public List<Transacao> consultarTransacoes() {
		return this.transacoes;
	}
	public List<Investimento> consultarInvestimentos() {
		return this.investimentos;
	}
	public void bloquearConta() {
		this.ativo = false;
	}
	public void depositarConta(double valor) {
		this.saldo += valor;
	}
	public void sacarConta(double valor) {
		this.saldo -= valor;
	}
}
