function getData(url = "" , onGet , onError){
    
    let headers = {
        "Content-Type": "application/json"
    };

    $.ajax({
        type:"get",
        url:url,
        headers: headers,
        dataType: "json",
        success: onGet,
        error: onError
    });

}

function postData(url = "" , data = {} , onGet , onError){
    let headers = {
        "Content-Type": "application/json"
    };

    $.ajax({
        contentType: "json",
        type:"post",
        url:url,
        headers: headers,
        data: JSON.stringify(data),
        dataType: "json",
        success: onGet,
        error: onError
    });


}