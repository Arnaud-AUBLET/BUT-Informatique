import java.util.ArrayList;

import ardoise.*;

public class Triangles extends Forme{
	
	private PointPlan pp1;
	private PointPlan pp2;
	private PointPlan pp3;
	
	public Triangles() {}
	
	public Triangles(PointPlan pp1, PointPlan pp2, PointPlan pp3) {
		this.pp1 = pp1;
		this.pp2 = pp2;
		this.pp3 = pp3;
	}
	
	public PointPlan getPp1() {return pp1;}
	
	public void setPp1(PointPlan pp) {
		this.pp1 = pp;
	}
	
	public PointPlan getPp2() {return pp2;}
	
	public void setPp2(PointPlan pp) {
		this.pp2 = pp;
	}
	
	public PointPlan getPp3() {return pp3;}
	
	public void setPp3(PointPlan pp) {
		this.pp3 = pp;
	}
	
	
	@Override
	public void deplacer(int deplacementX, int deplacementY) {
		this.pp1.deplacer(deplacementX, deplacementY);
		this.pp2.deplacer(deplacementX, deplacementY);
		this.pp3.deplacer(deplacementX, deplacementY);
	}

	@Override
	public ArrayList<Segment> dessiner() {
		ArrayList<Segment> liste = new ArrayList<Segment>();
		Segment s1 = new Segment(pp1, pp2);
		Segment s2 = new Segment(pp2, pp3);
		Segment s3 = new Segment(pp3, pp1);

		liste.add(s1);
		liste.add(s2);
		liste.add(s3);
		
		return liste;
	}

	@Override
	public String typeForme() {
		return "T";
	}

	
	
}
