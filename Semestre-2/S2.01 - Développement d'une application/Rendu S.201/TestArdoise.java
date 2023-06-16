import java.util.ArrayList;

import ardoise.*;

public class TestArdoise {

	public static void main(String[] args) throws InterruptedException{
		
		Ardoise ardoise = new Ardoise();

		Chapeaux oiseau1 = new Chapeaux(new PointPlan(118, 13), new PointPlan(123, 20), new PointPlan(128, 13));
		ardoise.ajouterForme(oiseau1);
		Chapeaux oiseau2 = new Chapeaux(new PointPlan(133, 30), new PointPlan(136, 32), new PointPlan(138, 30));
		ardoise.ajouterForme(oiseau2);
		Chapeaux oiseau3 = new Chapeaux(new PointPlan(142, 14), new PointPlan(144, 17), new PointPlan(146, 14));
		ardoise.ajouterForme(oiseau3);
		Quadrilatères tour = new Quadrilatères(new PointPlan(9, 100), new PointPlan(20, 198));
		ardoise.ajouterForme(tour);
		Quadrilatères corps = new Quadrilatères(new PointPlan(80, 140), new PointPlan(180, 198));
		Chapeaux toit = new Chapeaux(new PointPlan(80, 140), new PointPlan(130, 100), new PointPlan(180, 140));
		Quadrilatères porte = new Quadrilatères(new PointPlan(120, 170), new PointPlan(140, 198));
		GrandesFormes maison = new GrandesFormes();
		maison.addForme(corps);
		maison.addForme(toit);
		maison.addForme(porte);
		ardoise.ajouterForme(maison);
		Chapeaux etoile1 = new Chapeaux(new PointPlan(170, 52), new PointPlan(173, 45), new PointPlan(177, 52));
		Chapeaux etoile2 = new Chapeaux(new PointPlan(177, 52), new PointPlan(184, 57), new PointPlan(177, 60));
		Chapeaux etoile3 = new Chapeaux(new PointPlan(177, 60), new PointPlan(174, 66), new PointPlan(170, 60));
		Chapeaux etoile4 = new Chapeaux(new PointPlan(170, 60), new PointPlan(164, 57), new PointPlan(170, 52));
		ArrayList<Forme> fEtoile = new ArrayList<Forme>();
		fEtoile.add(etoile1);
		fEtoile.add(etoile2);
		fEtoile.add(etoile3);
		fEtoile.add(etoile4);
		GrandesFormes etoile = new GrandesFormes(fEtoile);
		ardoise.ajouterForme(etoile);
		System.out.println(etoile1.dessiner());
		System.out.println(etoile.dessiner());
		Triangles montagne1 = new Triangles(new PointPlan(3, 14), new PointPlan(43, 3), new PointPlan(112, 14));
		ardoise.ajouterForme(montagne1);
		Triangles montgnes2 = new Triangles(new PointPlan(152, 7), new PointPlan(166, 3), new PointPlan(172, 7));
		ardoise.ajouterForme(montgnes2);
		
		ardoise.dessinerGraphique();
		
		for (int i=0; i<8; i++) {
			Thread.sleep(1000);
			ardoise.deplacer("", 0, 0);
			oiseau1.deplacer(10, 20);
			oiseau2.deplacer(10, 20);
			oiseau3.deplacer(10, 20);
		}
	}

}
