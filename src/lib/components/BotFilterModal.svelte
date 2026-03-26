<script>
	import { onMount } from 'svelte';
	import Modal from '$lib/components/Modal.svelte';
	import { regionState } from '$lib/state/region.svelte';
	import { toastState } from '$lib/state/toast.svelte';

	let isBotFilterModalOpen = $state(false);
	let botFilterMountedTime = $state(0);
	let v_token = $state('');
	let activeCountry = $state('Россия');

	const showroomsData = {
		Беларусь: ['Минск', 'Гродно', 'Брест', 'Витебск', 'Гомель', 'Могилёв'],
		Россия: [
			'Москва и МО',
			'Санкт-Петербург',
			'Нижний Новгород',
			'Казань',
			'Екатеринбург',
			'Новосибирск',
			'Омск',
			'Тюмень',
			'Челябинск',
			'Уфа',
			'Самара',
			'Воронеж',
			'Краснодар',
			'Ростов-на-Дону',
			'Волгоград',
			'Пермь',
			'Красноярск'
		]
	};

	function handleCitySelect(city) {
		const timeTaken = Date.now() - botFilterMountedTime;

		// Silent check: honeypot or too fast (< 100ms)
		if (v_token !== '' || timeTaken < 100) {
			console.warn('Bot detected by silent check!');
			toastState.add({
				type: 'error',
				title: 'Ошибка',
				message: 'Обнаружена подозрительная активность. Действие заблокировано.'
			});
			return;
		}

		regionState.setCity(city);
		regionState.confirmCity();
		isBotFilterModalOpen = false;

		toastState.add({
			type: 'success',
			message: 'Город выбран'
		});
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
		<p class="text-sm text-secondary">
			Добро пожаловать на сайт мебельной фабрики ЗОВ! Для продолжения работы с сайтом выберите ваш
			город.
		</p>

		<!-- Honeypot: field with unobvious name to trap bots -->
		<input
			type="text"
			name="session_verification_token"
			class="absolute -left-9999 top-0 h-0 w-0 opacity-0"
			tabindex="-1"
			autocomplete="off"
			bind:value={v_token}
		/>

		<div class="flex items-center gap-4 border-b border-border-light pb-4">
			{#each Object.keys(showroomsData) as country}
				<button
					class="relative text-sm font-medium tracking-wide transition-colors duration-300 {activeCountry ===
					country
						? 'text-primary'
						: 'text-muted hover:text-secondary'}"
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

		<div class="grid max-h-[50vh] grid-cols-1 gap-3 overflow-y-auto pr-1 sm:max-h-none sm:grid-cols-3 sm:overflow-visible sm:pr-0">
			{#each showroomsData[activeCountry] as city}
				<button
					class="rounded-lg border border-border-light px-4 py-3 text-sm tracking-wide transition-all duration-300 {regionState.selectedCity ===
					city
						? 'border-primary bg-primary text-white'
						: 'bg-transparent text-secondary hover:border-primary hover:text-primary'}"
					onclick={() => handleCitySelect(city)}
				>
					{city}
				</button>
			{/each}
		</div>
	</div>
</Modal>
