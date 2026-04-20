from flask import Flask, render_template, request
from processing import generate_playmakers_scatter, generate_scorers_scatter, generate_wonderkid_bar, generate_player_radar, generate_reality_check_scatter, generate_league_dna_boxplot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/playmakers')
def playmakers():
    plot = generate_playmakers_scatter()
    
    return render_template('playmakers.html', plot=plot)

@app.route('/scorers')
def scorers():
    plot = generate_scorers_scatter()
    
    return render_template('scorers.html', plot=plot)

@app.route('/wonderkid')
def wonderkid():
    plot = generate_wonderkid_bar()

    return render_template('wonderkid.html', plot=plot)

@app.route('/player_radar',methods=['GET','POST'])
def player_radar():
    if request.method == 'POST':
        player1 = request.form.get('player_1')
        player2 = request.form.get('player_2')

        plot = generate_player_radar(player1,player2)
        return render_template('player_radar.html', plot=plot)
    return render_template('player_radar.html', plot='')

@app.route('/reality_check')
def reality_check():
    plot = generate_reality_check_scatter()

    return render_template('reality_check.html', plot=plot)

@app.route('/league_dna')
def league_dna():
    plot = generate_league_dna_boxplot()
    return render_template('league_dna.html', plot=plot)

if __name__ == '__main__':
    app.run(debug=True)