package fiap.fintech.financas;

import java.util.Date;

public class Transacao {
	int id;
	Conta contaOrigem;
	Conta contaDestino;
	Date data;
	double valor;
	String tipoTransacao;
	
	public Transacao( int id, Conta contaOrigem,Conta contaDestino, Date data,double valor,String tipoTransacao) {
		this.id = id;
		this.contaOrigem = contaOrigem;
		this.contaDestino = contaDestino;
		this.data = data;
		this.valor =valor;
		this.tipoTransacao = tipoTransacao;
	}
	
	public int consultarId() {
		return this.id;
	}
	public Conta consultarContaOrigem() {
		return this.contaOrigem;
	}
	public Conta consultarContaDestino() {
		return this.contaDestino;
	}
	public double consultarValor() {
		return this.valor;
	}
	public Date consultarData() {
		return this.data;
	}
	public String consultarTipoTransacao() {
		return this.tipoTransacao;
	}
}
