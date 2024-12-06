<div style="text-align:center;">
    <h2>
        River Monitoring
    </h2>
</div>
<div id="datacam1" style="text-align:center;">
    <img id="cam1" style="max-width:600px;width:100%;" />
</div>
<script>

    setInterval(() => {
        $("#cam1").attr('src', 'https://device.alfianrek.my.id/api/get/image/2ccf6729aa9e/');

    }, 300);


</script>