import http from 'k6/http';
import { sleep, check } from 'k6';

export let options = {
    stages: [
        { duration: '30s', target: 20 }, // ramp up to 20 users
        { duration: '1m', target: 20 },  // stay at 20 users
        { duration: '30s', target: 100 }, // scale up to 100 users (trigger HPA)
        { duration: '2m', target: 100 },
        { duration: '1m', target: 0 },   // scale down
    ],
};

export default function () {
    let res = http.get('http://localhost:80/users'); // Assuming Kong is at localhost:80
    check(res, {
        'status is 200': (r) => r.status === 200,
        'latency < 500ms': (r) => r.timings.duration < 500,
    });
    sleep(1);
}
