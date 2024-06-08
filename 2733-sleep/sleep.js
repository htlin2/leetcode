/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    const p = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('foo');
    }, millis)})
    return p
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */