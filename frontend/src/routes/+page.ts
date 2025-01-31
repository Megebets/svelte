export async function load({ fetch }) {
    const res = await fetch('http://127.0.0.1:8000/main-page/');
    if (res.ok) {
        const data = await res.json();
        return {
            props: data
        };
    } else {
        return {
            props: {
                error: 'Не удалось загрузить данные.'
            }
        };
    }
}
