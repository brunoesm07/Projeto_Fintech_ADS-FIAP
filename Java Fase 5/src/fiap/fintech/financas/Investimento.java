package fiap.fintech.financas;

import java.util.Date;

public class Investimento {
	int id;
	double valor;
	Conta conta;
	Date data;
	String tipoInvestimento;
	
	public Investimento( int id,double valor,Conta conta, Date data,String tipoInvestimento) {
		this.id = id;
		this.valor = valor;
		this.conta = conta;
		this.data = data;
		this.tipoInvestimento = tipoInvestimento;
	}
	
	public int consultarId() {
		return this.id;
	}
	public double consultarContaOrigem() {
		return this.valor;
	}
	public Conta consultarContaDestino() {
		return this.conta;
	}
	public Date consultarData() {
		return this.data;
	}
	public String consultarTipoTransacao() {
		return this.tipoInvestimento;
	}
}
