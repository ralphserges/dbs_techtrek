export function configureFakeBackend() {
    let users = [{ id: 1, username: 'caritativofiona', password: '922cb712bea79bc8', firstName: 'caritativo', lastName: 'fiona' }];
    

    // data = {
                //     'username': 'caritativofiona',
                //     'password': '922cb712bea79bc8'
                // }
    
    let realFetch = window.fetch;
    window.fetch = function (url, opts) {
        const isLoggedIn = opts.headers['Authorization'] === 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNhcml0YXRpdm9maW9uYSIsImlhdCI6MTYwMDk5OTQ4NiwiZXhwIjoxNjAxMDAwMDg2LCJpc3MiOiJ0ZWNodHJlazIwMjAifQ.XwRWQe4wrNQRWzHuxpArgu6hxrrkI6gyUOAX9V4n4tn4r7hdqOByaZu-5_SOJ3awwCzC06_CQh3mEbv1FalX9A';

        return new Promise((resolve, reject) => {
            // wrap in timeout to simulate server api call
            setTimeout(() => {
                // authenticate - public
                if (url.endsWith('/users/authenticate') && opts.method === 'POST') {
                    const params = JSON.parse(opts.body);
                    const user = users.find(x => x.username === params.username && x.password === params.password);
                    if (!user) return error('Username or password is incorrect');
                    return ok({
                        id: user.id,
                        username: user.username,
                        firstName: user.firstName,
                        lastName: user.lastName,
                        token: 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNhcml0YXRpdm9maW9uYSIsImlhdCI6MTYwMDk5OTQ4NiwiZXhwIjoxNjAxMDAwMDg2LCJpc3MiOiJ0ZWNodHJlazIwMjAifQ.XwRWQe4wrNQRWzHuxpArgu6hxrrkI6gyUOAX9V4n4tn4r7hdqOByaZu-5_SOJ3awwCzC06_CQh3mEbv1FalX9A'
                    });
                    
                }

                

                // get users - secure
                if (url.endsWith('/users') && opts.method === 'GET') {
                    if (!isLoggedIn) return unauthorised();
                    return ok(users);
                }

                // pass through any requests not handled above
                realFetch(url, opts).then(response => resolve(response));

                // private helper functions

                function ok(body) {
                    resolve({ ok: true, text: () => Promise.resolve(JSON.stringify(body)) })
                }

                function unauthorised() {
                    resolve({ status: 401, text: () => Promise.resolve(JSON.stringify({ message: 'Unauthorised' })) })
                }

                function error(message) {
                    resolve({ status: 400, text: () => Promise.resolve(JSON.stringify({ message })) })
                }
            }, 500);
        });
    }
}