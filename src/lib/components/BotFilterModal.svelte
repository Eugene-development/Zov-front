<script>
	import { onMount } from 'svelte';
	import Modal from '$lib/components/Modal.svelte';
	import { regionState } from '$lib/state/region.svelte';

	let isBotFilterModalOpen = $state(false);
	let botFilterMountedTime = $state(0);
	let honeypotValue = $state('');
	let activeCountry = $state('Россия');

	const showroomsData = {
		Беларусь: ['Минск', 'Гродно'],
		Россия: ['Москва', 'Санкт-Петербург']
	};

	function handleCitySelect(city) {
		const timeTaken = Date.now() - botFilterMountedTime;

		// Silent check: honeypot or too fast (< 100ms)
		if (honeypotValue !== '' || timeTaken < 100) {
			console.warn('Bot detected by silent check!');
			alert('Обнаружена подозрительная активность. Действие заблокировано.');
			return;
		}

		regionState.setCity(city);
		regionState.confirmCity();
		isBotFilterModalOpen = false;
	}

	onMount(() => {
		if (!regionState.hasConfirmedCity) {
			setTimeout(() => {
				// double check in case they navigated or somehow confirmed before timeout fired
				if (!regionState.hasConfirmedCity) {
					isBotFilterModalOpen = true;
					botFilterMountedTime = Date.now();
				}
			}, 5000);
		}
	});
</script>

<Modal bind:showModal={isBotFilterModalOpen} title="Выберите ваш город" dismissible={false}>
	<div class="flex flex-col gap-6">
		<p class="text-sm text-text-secondary">
			Добро пожаловать на сайт фабрики! Для продолжения работы с сайтом выберите ваш город.
		</p>

		<!-- Honeypot -->
		<input
			type="text"
			name="website_url"
			style="display: none;"
			tabindex="-1"
			autocomplete="off"
			bind:value={honeypotValue}
		/>

		<div class="flex items-center gap-4 border-b border-border-light pb-4">
			{#each Object.keys(showroomsData) as country}
				<button
					class="relative text-sm font-medium tracking-wide transition-colors duration-300 {activeCountry ===
					country
						? 'text-primary'
						: 'text-text-muted hover:text-text-secondary'}"
					onclick={() => (activeCountry = country)}
				>
					{country}
					{#if activeCountry === country}
						<span class="absolute -bottom-[17px] left-0 h-px w-full animate-fade-in bg-primary"
						></span>
					{/if}
				</button>
			{/each}
		</div>

		<div class="grid grid-cols-2 gap-3 sm:grid-cols-2">
			{#each showroomsData[activeCountry] as city}
				<button
					class="rounded-lg border border-border-light px-4 py-3 text-sm tracking-wide transition-all duration-300 {regionState.selectedCity ===
					city
						? 'border-primary bg-primary text-white'
						: 'bg-transparent text-text-secondary hover:border-primary hover:text-primary'}"
					onclick={() => handleCitySelect(city)}
				>
					{city}
				</button>
			{/each}
		</div>
	</div>
</Modal>
