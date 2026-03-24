<script>
	import { onMount } from 'svelte';
	import Modal from '$lib/components/Modal.svelte';
	import DesignerForm from '$lib/components/DesignerForm.svelte';
	import ShowroomForm from '$lib/components/ShowroomForm.svelte';

	let heroVisible = $state(false);
	let isDesignerModalOpen = $state(false);
	let isShowroomModalOpen = $state(false);
	let sections = $state({});
	let activeCountry = $state('Беларусь');
	let activeCity = $state('Все');
	let mapContainer = $state(null);
	let mapInstance = $state(null);

	onMount(() => {
		heroVisible = true;

		const observer = new IntersectionObserver(
			(entries) => {
				entries.forEach((entry) => {
					if (entry.isIntersecting) {
						sections[entry.target.id] = true;
					}
				});
			},
			{ threshold: 0.15, rootMargin: '0px 0px -50px 0px' }
		);

		// Initialize Map
		function initMap() {
			if (!mapContainer || typeof window.ymaps === 'undefined') return;
			mapInstance = new window.ymaps.Map(mapContainer, {
				center: [54.5, 31.0],
				zoom: 5,
				controls: ['zoomControl', 'fullscreenControl']
			});
		}

		if (window.ymaps) {
			window.ymaps.ready(initMap);
		} else {
			let script = document.querySelector('script[src*="api-maps.yandex.ru"]');
			if (!script) {
				script = document.createElement('script');
				script.src = 'https://api-maps.yandex.ru/2.1/?lang=ru_RU';
				document.head.appendChild(script);
			}
			script.addEventListener('load', () => {
				window.ymaps.ready(initMap);
			});
		}

		document.querySelectorAll('[data-animate]').forEach((el) => {
			observer.observe(el);
		});

		return () => {
			observer.disconnect();
			if (mapInstance) {
				mapInstance.destroy();
			}
		};
	});

	const showrooms = {
		Беларусь: [
			{
				city: 'Гродно',
				places: [
					{
						name: 'Флагманский салон ЗОВ',
						address: 'ул. Индустриальная, 9',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: [53.649, 23.823]
					}
				]
			},
			{
				city: 'Минск',
				places: [
					{
						name: 'ТЦ «Замок Home»',
						address: 'пр-т Победителей, 65, 4 этаж',
						hours: 'Пн-Вс: 10:00 – 22:00',
						coords: [53.926, 27.518]
					},
					{
						name: 'ТЦ «Камелот»',
						address: 'ул. Мазурова, 1',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: [53.890632, 27.433431]
					}
				]
			}
		],
		Россия: [
			{
				city: 'Москва',
				places: [
					{
						address: 'Подольское ш., д. 8, корп. 5',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: [55.709324, 37.653457]
					},
					{
						address: 'Ленинградский пр-т, д. 74, корп. 1',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: [55.805133, 37.516952]
					}
				]
			},
			{
				city: 'Санкт-Петербург',
				places: [
					{
						name: 'ТЦ «Мебельный Континент»',
						address: 'ул. Варшавская, 3',
						hours: 'Пн-Вс: 10:00 – 20:00',
						coords: [59.882, 30.312]
					}
				]
			}
		]
	};

	let availableCities = $derived(['Все', ...showrooms[activeCountry].map((d) => d.city)]);
	let filteredShowrooms = $derived(
		activeCity === 'Все'
			? showrooms[activeCountry]
			: showrooms[activeCountry].filter((d) => d.city === activeCity)
	);

	let totalPlaces = $derived(filteredShowrooms.reduce((acc, curr) => acc + curr.places.length, 0));

	$effect(() => {
		if (!mapInstance || typeof window.ymaps === 'undefined') return;
		
		mapInstance.geoObjects.removeAll();
		
		filteredShowrooms.forEach((city) => {
			city.places.forEach((place) => {
				if (place.coords) {
					const placemark = new window.ymaps.Placemark(
						place.coords,
						{
							balloonContentHeader: place.name || 'Салон ЗОВ',
							balloonContentBody: place.address,
							balloonContentFooter: place.hours
						},
						{
							preset: 'islands#blueIcon'
						}
					);
					mapInstance.geoObjects.add(placemark);
				}
			});
		});

		const bounds = mapInstance.geoObjects.getBounds();
		if (bounds) {
			mapInstance.setBounds(bounds, {
				checkZoomRange: true,
				zoomMargin: 50,
				duration: 400
			}).then(() => {
				if (mapInstance.getZoom() > 15) {
					mapInstance.setZoom(15);
				}
			});
		} else {
            mapInstance.setCenter([54.5, 31.0], 5);
        }
	});
</script>

<svelte:head>
	<title>Салоны ЗОВ | Адреса в России и Беларуси</title>
	<meta
		name="description"
		content="Найдите ближайший фирменный салон мебели ЗОВ в вашем городе. Более 120 салонов в России и Беларуси. Адреса, контакты, время работы и интерактивная карта."
	/>
</svelte:head>

<!-- ==================== HERO SECTION ==================== -->
<section class="relative min-h-[90vh] overflow-hidden bg-surface" id="hero">
	<!-- Background Image -->
	<div class="absolute inset-0">
		<img
			src="/images/modern_showroom.png"
			alt="Интерьер салона ЗОВ"
			class="h-full w-full object-cover transition-transform duration-[2s]"
			class:scale-105={heroVisible}
		/>
		<div
			class="absolute inset-0 bg-gradient-to-r from-primary/90 via-primary/60 to-transparent"
		></div>
	</div>

	<!-- Content -->
	<div class="relative z-10 flex min-h-[90vh] items-center">
		<div class="mx-auto w-full max-w-7xl px-6">
			<div class="max-w-xl">
				<div
					class="mb-6 opacity-0"
					class:animate-fade-up={heroVisible}
					style="animation-delay: 0.3s"
				>
					<span class="text-[11px] tracking-[0.3em] text-white/70 uppercase">Где купить</span>
				</div>
				<h1
					class="text-5xl leading-[1.1] font-light text-white opacity-0 md:text-6xl lg:text-7xl"
					style="font-family: var(--font-heading); animation-delay: 0.5s"
					class:animate-fade-up={heroVisible}
				>
					Наши <span class="text-accent-light">салоны</span>
				</h1>
				<p
					class="mt-6 text-base leading-relaxed text-white/70 opacity-0 md:text-lg"
					class:animate-fade-up={heroVisible}
					style="animation-delay: 0.7s"
				>
					Посетите один из наших фирменных салонов. Оцените качество материалов вживую, вдохновитесь
					готовыми интерьерными решениями и создайте проект вашей кухни вместе с профессиональными
					дизайнерами.
				</p>
				<div
					class="mt-10 opacity-0"
					class:animate-fade-up={heroVisible}
					style="animation-delay: 0.9s"
				>
					<a
						href="#network-section"
						class="group inline-flex cursor-pointer items-center gap-3 rounded-sm border border-secondary bg-secondary px-8 py-4 text-xs tracking-[0.15em] text-white uppercase transition-all duration-500 hover:bg-transparent"
					>
						Посмотреть карту
						<svg
							class="h-4 w-4 transition-transform duration-300 group-hover:translate-y-1"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
							stroke-width="1.5"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								d="M19.5 13.5 12 21m0 0-7.5-7.5M12 21V3"
							/>
						</svg>
					</a>
				</div>
			</div>
		</div>
	</div>

	<!-- Scroll Indicator -->
	<div
		class="absolute bottom-10 left-1/2 -translate-x-1/2 opacity-0"
		class:animate-fade-in={heroVisible}
		style="animation-delay: 1.3s"
	>
		<div class="flex flex-col items-center gap-2">
			<span class="text-[10px] tracking-[0.3em] text-white/50 uppercase">Вниз</span>
			<div class="h-10 w-px bg-gradient-to-b from-white/50 to-transparent"></div>
		</div>
	</div>
</section>

<!-- ==================== MAP & LIST SECTION ==================== -->
<section
	class="relative scroll-mt-20 bg-surface py-section lg:scroll-mt-24"
	id="network-section"
	data-animate
>
	<div class="mx-auto max-w-7xl px-6">
		<div class="grid gap-16 lg:grid-cols-12 lg:gap-12">
			<!-- Left Column: Locations List -->
			<div
				class="flex flex-col opacity-0 lg:col-span-5"
				class:animate-fade-up={sections['network-section']}
			>
				<h2
					class="text-3xl font-light text-primary lg:text-4xl"
					style="font-family: var(--font-heading);"
				>
					Дилерская сеть салонов в Беларуси и России
				</h2>

				<!-- Country Toggle -->
				<div class="mt-8 flex items-center gap-4 border-b border-border-light pb-4">
					{#each Object.keys(showrooms) as country (country)}
						<button
							class="relative text-sm font-medium tracking-wide transition-colors duration-300 {activeCountry ===
							country
								? 'text-primary'
								: 'text-muted hover:text-secondary'}"
							onclick={() => {
								activeCountry = country;
								activeCity = 'Все';
							}}
						>
							{country}
							{#if activeCountry === country}
								<span
									class="absolute -bottom-[17px] left-0 h-px w-full bg-primary"
									class:animate-fade-in={true}
								></span>
							{/if}
						</button>
					{/each}
				</div>

				<!-- City Filter -->
				<div class="mt-6 flex flex-wrap gap-2">
					{#each availableCities as city (city)}
						<button
							class="rounded-sm border border-border-light px-4 py-1.5 text-xs tracking-wide transition-colors duration-300 {activeCity ===
							city
								? 'border-primary bg-primary text-white'
								: 'bg-transparent text-secondary hover:border-text-muted hover:text-primary'}"
							onclick={() => (activeCity = city)}
						>
							{city}
						</button>
					{/each}
				</div>

				<!-- Cities List -->
				<div class="relative -mx-2 mt-8 px-2">
					<div
						class="flex flex-col gap-10 {totalPlaces > 3
							? 'max-h-[550px] overflow-y-auto pr-4 pb-10 [&::-webkit-scrollbar]:w-1.5 [&::-webkit-scrollbar-thumb]:rounded-full [&::-webkit-scrollbar-thumb]:bg-border-light/80 hover:[&::-webkit-scrollbar-thumb]:bg-border-light [&::-webkit-scrollbar-track]:bg-transparent'
							: ''}"
					>
						{#each filteredShowrooms as data (data.city)}
							<div>
								<h3
									class="flex items-center gap-3 text-xl font-medium text-primary"
									style="font-family: var(--font-heading);"
								>
									<svg
										class="h-5 w-5 text-secondary"
										fill="none"
										viewBox="0 0 24 24"
										stroke="currentColor"
										stroke-width="1.5"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z"
										/>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z"
										/>
									</svg>
									{data.city}
								</h3>

								<div class="mt-6 flex flex-col gap-6">
									{#each data.places as place, i ((place.name ?? place.address) + i)}
										<div
											class="group border-l-2 border-border-light pl-6 transition-colors duration-300 hover:border-secondary"
										>
											{#if place.name}
												<h4 class="text-base font-medium text-primary">{place.name}</h4>
											{/if}
											<p class="{place.name ? 'mt-2' : ''} text-sm text-secondary">
												{place.address}
											</p>
											<div class="mt-4 flex flex-col gap-1.5 text-xs text-muted">
												<div class="flex items-center gap-2">
													<svg
														class="h-3.5 w-3.5"
														fill="none"
														viewBox="0 0 24 24"
														stroke="currentColor"
														stroke-width="1.5"
													>
														<path
															stroke-linecap="round"
															stroke-linejoin="round"
															d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"
														/>
													</svg>
													{place.hours}
												</div>
											</div>
										</div>
									{/each}
								</div>
							</div>
						{/each}
					</div>
					{#if totalPlaces > 3}
						<div
							class="pointer-events-none absolute bottom-0 left-0 h-24 w-full bg-gradient-to-t from-surface to-transparent"
						></div>
					{/if}
				</div>

				<div class="mt-10 flex">
					<button
						onclick={() => (isShowroomModalOpen = true)}
						class="group inline-flex cursor-pointer items-center gap-3 rounded-sm border border-border-medium px-6 py-3 text-xs tracking-[0.15em] text-primary uppercase transition-all duration-500 hover:border-secondary hover:text-secondary"
					>
						Запись в салон
						<svg
							class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
							stroke-width="1.5"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"
							/>
						</svg>
					</button>
				</div>
			</div>

			<!-- Right Column: Yandex Interactive Map -->
			<div
				class="h-[600px] opacity-0 lg:col-span-7 lg:h-[750px]"
				class:animate-fade-up={sections['network-section']}
				style="animation-delay: 0.3s"
			>
				<div class="relative h-full w-full overflow-hidden bg-surface-warm shadow-soft">
					<div
						bind:this={mapContainer}
						class="absolute inset-0 contrast-125 grayscale transition-all duration-700 hover:grayscale-0"
					></div>
				</div>
			</div>
		</div>
	</div>
</section>

<!-- ==================== CTA SECTION ==================== -->
<section
	class="relative overflow-hidden bg-primary py-section-sm lg:py-section"
	id="cta-section"
	data-animate
>
	<div
		class="absolute inset-0 opacity-[0.03]"
		style="background-image: url('data:image/svg+xml,%3Csvg width=\'60\' height=\'60\' viewBox=\'0 0 60 60\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cg fill=\'none\' fill-rule=\'evenodd\'%3E%3Cg fill=\'%23ffffff\'%3E%3Cpath d=\'M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z\'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E');"
	></div>

	<div class="relative mx-auto max-w-4xl px-6 text-center">
		<div class="opacity-0" class:animate-fade-up={sections['cta-section']}>
			<h2
				class="text-3xl font-light text-white lg:text-5xl"
				style="font-family: var(--font-heading);"
			>
				Нет времени на поездку в салон?
			</h2>
			<p class="mx-auto mt-6 max-w-2xl text-base leading-relaxed text-white/70">
				Закажите выезд дизайнера на дом абсолютно бесплатно. Наш специалист приедет с образцами
				фасадов и столешниц, снимет точные замеры и создаст 3D-проект вашей будущей кухни прямо на
				месте.
			</p>

			<div class="mt-10 flex flex-wrap items-center justify-center gap-4">
				<button
					onclick={() => (isDesignerModalOpen = true)}
					class="group inline-flex cursor-pointer items-center gap-3 rounded-sm border border-secondary bg-secondary px-8 py-4 text-xs tracking-[0.15em] text-white uppercase transition-all duration-500 hover:bg-transparent hover:text-secondary"
				>
					Вызвать дизайнера
					<svg
						class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
						stroke-width="1.5"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"
						/>
					</svg>
				</button>
			</div>
		</div>
	</div>
</section>

<!-- Modals -->
<Modal bind:showModal={isDesignerModalOpen} title="Вызов дизайнера">
	<DesignerForm onSuccess={() => (isDesignerModalOpen = false)} />
</Modal>

<Modal bind:showModal={isShowroomModalOpen} title="Запись в салон">
	<ShowroomForm onSuccess={() => (isShowroomModalOpen = false)} />
</Modal>
