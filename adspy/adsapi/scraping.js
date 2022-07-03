const cheerio = require("cheerio");
const axios = require("axios");

const url="https://www.facebook.com/ads/archive/render_ad/?id=402810998437834&access_token=EAAOmIkyczYcBAMImAvB1WYR7OBptnUgWDZC4VqutpZAZCtAcfbVyXD5vmMQVRLjWr6iOXO6T7ZAWVXGwnffb8asseZB6ZBOlUnUMq8JDEuZAO9Ltxp3vGMxydFb8ZCr70WuFa7FpBXHEYvl1yq9MZBCqImGMS5o4sImhw5ZAnCMfiIVrcdnD9j4BDnZAPNpv2MDPDf5mbXy9clBWVzJb7KlDoBxNKsUcZAO83vsorkuVm8shIOZAPhIUGB0NgbUOoMg0DgZAcNMZCMXjVeeDQZDZD";

async function getGenre(){
   try{
        const response = await axios.get(url);
        const $=cheerio.load(response.data);
        const genre=$("qIDrmlRXOr").text();

        console.log(genre);
        
    }
    catch(error){
        console.error(error);


    }

}
getGenre();
