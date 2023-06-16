import java.util.ArrayList;

import ardoise.*;

public class GrandesFormes extends Forme {

	private ArrayList<Forme> lf;
	
	GrandesFormes() {
		this.lf = new ArrayList<Forme>();
	}
	
	GrandesFormes(ArrayList<Forme> lf) {
		this.lf = lf;
	}
	
	@Override
	public void deplacer(int deplacementX, int deplacementY) {
		for (int i = 0; i<lf.size(); i++) {
			lf.get(i).deplacer(deplacementX, deplacementY);
		}
	}

	@Override
	public ArrayList<Segment> dessiner() {
		ArrayList<Segment> liste = new ArrayList<Segment>();
		
		for (int i=0; i<lf.size();i++) {
			ArrayList<Segment> temp = lf.get(i).dessiner();
			for (int j=0; j<temp.size(); j++) {
				liste.add(temp.get(j));
			}
		}
		return liste;
	}

	@Override
	public String typeForme() {
		return "GF";
	}

	public ArrayList<Forme> getLf() {
		return lf;
	}

	public void setLf(ArrayList<Forme> lf) {
		this.lf = lf;
	}
	
	public void addForme(Forme f) {
		this.lf.add(f);
	}

}
