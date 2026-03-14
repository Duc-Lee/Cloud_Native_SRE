import http from 'k6/http';
import { sleep, check } from 'k6';

export let options = {
    stages: [
        { duration: '30s', target: 10 },
        { duration: '1m', target: 10 },
        { duration: '30s', target: 50 },
        { duration: '1m', target: 50 },
        { duration: '30s', target: 0 },
    ],
};

export default function () {
    // Testing via Nginx Gateway
    let res = http.get('http://localhost:80/user');
    check(res, {
        'status is 200': (r) => r.status === 200,
        'latency < 200ms': (r) => r.timings.duration < 200,
    });
    sleep(1);
}
