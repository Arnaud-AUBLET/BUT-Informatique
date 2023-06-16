import java.util.ArrayList;

import ardoise.*;

public class Quadrilatères extends Forme{
	
	private PointPlan pp1;
	private PointPlan pp3;

	public Quadrilatères() {}
	
	public Quadrilatères(PointPlan pp1, PointPlan pp3) {
		this.pp1 = pp1;
		this.pp3 = pp3;
		
	}
	
	@Override
	public void deplacer(int deplacementX, int deplacementY) {
		this.pp1.deplacer(deplacementX, deplacementY);

		this.pp3.deplacer(deplacementX, deplacementY);
	}

	@Override
	public ArrayList<Segment> dessiner() {
		PointPlan pp2 = new PointPlan(pp3.getAbscisse(), pp1.getOrdonnee());
		PointPlan pp4 = new PointPlan(pp1.getAbscisse(), pp3.getOrdonnee());
		Segment s1 = new Segment(pp1, pp2);
		Segment s2 = new Segment(pp2, pp3);
		Segment s3 = new Segment(pp3, pp4);
		Segment s4 = new Segment(pp4, pp1);
		ArrayList<Segment> liste = new ArrayList<Segment>();
		
		liste.add(s1);
		liste.add(s2);
		liste.add(s3);
		liste.add(s4);
		return liste;
	}

	@Override
	public String typeForme() {
		return "Q";
	}

	public PointPlan getPp1() {
		return pp1;
	}

	public void setPp1(PointPlan pp1) {
		this.pp1 = pp1;
	}

	public PointPlan getPp3() {
		return pp3;
	}

	public void setPp3(PointPlan pp3) {
		this.pp3 = pp3;
	}
	
}
