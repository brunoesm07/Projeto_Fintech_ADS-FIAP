package fiap.fintech.financas;

import java.util.Date;

public class Movimentacao {
	String tituloMovimentacao;
	double valorMovimentacao;
	Date data;
	boolean eReceita;
	
	public Movimentacao(String tituloMovimentacao, double valorMovimentacao , Date data, boolean eReceita) {
		this.valorMovimentacao = valorMovimentacao;
		this.tituloMovimentacao = tituloMovimentacao;
		this.data = data;
		this.eReceita = eReceita;
	}
	
	public String tipoMovimentacao() {
		if(this.eReceita) {
			return "Receita";
		}
		return "Despesa";
	}
	public double consultarValorMovimentacao() {
		return this.valorMovimentacao;
	}
	public String consultarTituloMovimentacao() {
		return this.tituloMovimentacao;
	}
	public Date consultardata() {
		return this.data;
	}

}
