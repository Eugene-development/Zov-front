<script>
	import './layout.css';
	import Header from '$lib/components/Header.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import ToastContainer from '$lib/components/ToastContainer.svelte';
	import BotFilterModal from '$lib/components/BotFilterModal.svelte';
	import { afterNavigate } from '$app/navigation';
	import { tick } from 'svelte';
	import { dev } from '$app/environment';

	let { children } = $props();

	afterNavigate(async () => {
		if (window.location.hash) {
			await tick();
			setTimeout(() => {
				const el = document.querySelector(window.location.hash);
				if (el) {
					el.scrollIntoView({ behavior: 'smooth' });
				}
			}, 150);
		}
	});
</script>

<svelte:head>
	<!-- {#if !dev} -->
	{#if true}
		<!-- Yandex.Metrika counter -->
		<script type="text/javascript">
			(function (m, e, t, r, i, k, a) {
				m[i] = m[i] || function () { (m[i].a = m[i].a || []).push(arguments) };
				m[i].l = 1 * new Date();
				for (var j = 0; j < document.scripts.length; j++) { if (document.scripts[j].src === r) { return; } }
				k = e.createElement(t), a = e.getElementsByTagName(t)[0], k.async = 1, k.src = r, a.parentNode.insertBefore(k, a)
			})
				(window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");

			ym(93835019, "init", {
				clickmap: true,
				trackLinks: true,
				accurateTrackBounce: true,
				webvisor: true
			});
		</script>
		<noscript>
			<div><img src="https://mc.yandex.ru/watch/93835019" style="position:absolute; left:-9999px;" alt="" /></div>
		</noscript>
		<!-- /Yandex.Metrika counter -->
	{/if}
</svelte:head>

<div class="flex min-h-screen flex-col">
	<Header />
	<main class="flex-1">
		{@render children()}
	</main>
	<Footer />

	<ToastContainer />
	<BotFilterModal />
</div>
