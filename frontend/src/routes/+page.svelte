<script>
    export let data;
</script>

<main>
    <h1>Ассаламу Алейкум</h1>
    {#if data}
        <p>Данные с сервера: {JSON.stringify(data)}</p>
    {/if}
</main>