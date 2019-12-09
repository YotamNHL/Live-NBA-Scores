/* Pulls the most updated data for the latest games the last 24 hours via the REST api flask server. */
const getLatestGames = (requested_team_name) => {
    var url = ""
    if (requested_team_name == "") {
            url = "http://localhost:5000/games?Team="
    }
    else {
        url = 'http://localhost:5000/games?Team=' + requested_team_name
    }
    return fetch(url)
    .then(res => res.json())
    .then(data => data);
} 

module.exports = {
    getLatestGames
}