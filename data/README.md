`tournaments.pickle`: Dictionary (k,v) (tournament-id, tournament-name) (ex. "i-m-not-yelling-feat-armada", "I'm Not Yelling! feat. ARMADA")

Note: smash.gg lists 1514 tournaments. For some reason only ~1510 get scraped.

`participants.pickle`: List of tuples (tournament-id, participant-id, participant-name) (ex. ('tgl-monthly-14', '637416', 'Krouton') )

Note: Some API calls (for some tournament ids) failed, so there are fewer unique tournaments in the participants list than in tournaments.pickle
