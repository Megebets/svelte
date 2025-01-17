export async function load({ fetch }) {
    const res = await fetch('http://127.0.0.1:8000/api/main-page/');
    if (res.ok) {
        const data = await res.json();
        return { data };
    }
    return { data: null };
}
