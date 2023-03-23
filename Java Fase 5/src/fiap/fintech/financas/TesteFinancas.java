package fiap.fintech.financas;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import fiap.fintech.financas.Movimentacao;

public class TesteFinancas {

	public static void main(String[] args) {
		User caio = new User(1,"caio","caio@gmail.com","1234","11111","99812042");
		Movimentacao loteria = new Movimentacao("ganhei na loteria", 1000, new Date(), true);
		Movimentacao vendicarro = new Movimentacao("vendi meu carro", 100, new Date(), false);
		Movimentacao vendicasa = new Movimentacao("vendi minha casa", 100, new Date(), false);
		
		List<Movimentacao> listMov = new ArrayList<Movimentacao>() ;
		listMov.add(vendicarro);
		listMov.add(vendicasa);
		listMov.add(loteria);
		
		int saldo = 0 ;
		
		for(int i = 0; i < listMov.size(); i++){
			System.out.println(listMov.get(i).tituloMovimentacao);
			if(listMov.get(i).eReceita) {
				saldo += listMov.get(i).valorMovimentacao;
			}
			else {
				saldo -= listMov.get(i).valorMovimentacao;
			}
			
		}
		System.out.println(saldo);

	}

}
