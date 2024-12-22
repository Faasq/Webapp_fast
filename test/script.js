import http from 'k6/http'
import { sleep,check } from 'k6'

export const options = {
    stages: [
        {duration:'5s',target:10},
        {duration:'10s',target:10},
    ]
}

export  default function(){
    const res = http.get('http://web:3000')
    check(res, { 'success login': (r) => r.status === 200 })
    sleep(1)
}