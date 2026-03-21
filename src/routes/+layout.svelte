<script>
	import './layout.css';
	import Header from '$lib/components/Header.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import ToastContainer from '$lib/components/ToastContainer.svelte';
	import BotFilterModal from '$lib/components/BotFilterModal.svelte';
	import { afterNavigate } from '$app/navigation';
	import { tick } from 'svelte';

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

<div class="flex min-h-screen flex-col">
	<Header />
	<main class="flex-1">
		{@render children()}
	</main>
	<Footer />

	<ToastContainer />
	<BotFilterModal />
</div>
