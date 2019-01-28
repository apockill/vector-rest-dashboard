class ApiEndpoint {
    constructor(url) {
        this._url = url;

        // Keep track whether this url is being called right now
        this.ongoing = false;
    }

    post(body) {
        return fetch(this._url, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(body)
        }).then(res => res.json())
    }

    get() {
        return fetch(this._url).then(res => res.json())
    }
}

export default ApiEndpoint