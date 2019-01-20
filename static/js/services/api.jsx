export function post(endpoint, body) {
    return fetch(`/api/${endpoint}`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(body)
    }).then(res => res.json())
}

export function get(endpoint) {
    return fetch(`/api/${endpoint}`).then(res => res.json())
}
