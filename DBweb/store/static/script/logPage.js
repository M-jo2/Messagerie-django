'use strict'
//import {getData , postData} from './api.js';

const API_URL_MESSAGERIE = "/messagerie"

$(document).ready(function(){

    $("#button-log").click(e => {
        console.log($("#log-username").val())
        getData(API_URL_MESSAGERIE , reponse , onerreur)

    })
    
})


function reponse(){
    console.log("a repondu")
}

function onerreur(){
    console.log("a pas repondu")
}