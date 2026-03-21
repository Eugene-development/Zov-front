<script>
	import { fade, fly } from 'svelte/transition';
	import { onMount } from 'svelte';
	import Modal from '$lib/components/Modal.svelte';
	import ShowroomForm from '$lib/components/ShowroomForm.svelte';

	let isVisible = $state(false);
	let isShowroomModalOpen = $state(false);

	onMount(() => {
		isVisible = true;
	});

	const features = [
		{
			title: 'Точные замеры',
			desc: 'Лазерное 3D-сканирование помещения для идеального встраивания',
			colSpan: 'col-span-1 md:col-span-2'
		},
		{
			title: 'Премиум фурнитура',
			desc: 'Бесшумное скольжение и доводчики от ведущих брендов',
			colSpan: 'col-span-1 md:col-span-1'
		},
		{
			title: 'Надежные материалы',
			desc: 'Экологичные плиты европейского стандарта высокой плотности',
			colSpan: 'col-span-1 md:col-span-1'
		},
		{
			title: 'Сложная архитектура',
			desc: 'Проектируем наполнение, учитывая ваш гардероб и обувь до мелочей',
			colSpan: 'col-span-1 md:col-span-2'
		}
	];
</script>

<svelte:head>
	<title>Шкафы и гардеробные | ЗОВ</title>
	<meta
		name="description"
		content="Премиальные шкафы и гардеробные системы фабрики ЗОВ. Индивидуальные проекты, идеальная геометрия и долговечность."
	/>
</svelte:head>

<main class="min-h-screen bg-surface-warm">
	<!-- Hero: Split Layout -->
	<section class="grid min-h-[70vh] lg:grid-cols-2">
		<div class="flex shrink-0 flex-col justify-center bg-white px-8 py-16 lg:px-20">
			{#if isVisible}
				<div in:fly={{ x: -30, duration: 1000, delay: 100 }}>
					<span class="mb-6 block text-sm font-medium tracking-[0.3em] text-accent uppercase"
						>Системы хранения</span
					>
					<h1
						class="mb-8 text-4xl leading-tight font-light tracking-wide text-primary lg:text-6xl"
						style="font-family: var(--font-heading);"
					>
						Идеальный порядок
						<br />
						<span class="text-secondary">в каждой детали</span>
					</h1>
					<p class="mb-12 max-w-lg text-lg leading-relaxed text-secondary">
						Мы создаем уникальные встроенные и корпусные шкафы, которые становятся органичным
						продолжением вашей квартиры. Максимальная вместимость и премиальная эстетика внутреннего
						пространства.
					</p>
					<a
						href="/showrooms"
						class="group inline-flex cursor-pointer items-center gap-3 border border-primary bg-primary px-8 py-4 text-xs tracking-[0.15em] text-white uppercase transition-all duration-500 hover:bg-transparent hover:text-primary rounded-sm"
					>
						Спроектировать шкаф
						<svg class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="1.5"
								d="M14 5l7 7m0 0l-7 7m7-7H3"
							/>
						</svg>
					</a>
				</div>
			{/if}
		</div>
		<div class="relative hidden overflow-hidden bg-border-light lg:block">
			<!-- Hero Placeholder Diagram inside -->
			<div class="absolute inset-0 flex flex-col items-center justify-center text-primary/30">
				<svg
					class="mb-6 h-32 w-32 opacity-30"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="1"
						d="M4 5a1 1 0 011-1h14a1 1 0 011 1v14a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 12h16M12 4v16"
					/>
				</svg>
				<span class="text-sm font-medium tracking-[0.2em] uppercase"
					>Заглушка: Большое фото роскошного шкафа</span
				>
			</div>
		</div>
	</section>

	<!-- Bento Box Features (Difference in structure from Kitchens) -->
	<section class="mx-auto max-w-7xl px-6 py-24">
		<div class="mb-16 text-center">
			<h2
				class="text-3xl font-light tracking-wide text-primary lg:text-4xl"
				style="font-family: var(--font-heading);"
			>
				Безупречное качество от замера до установки
			</h2>
		</div>

		<div class="grid grid-cols-1 gap-6 md:grid-cols-3">
			{#each features as feature, i}
				<div
					class="relative flex min-h-[250px] flex-col justify-end overflow-hidden rounded-3xl bg-white p-10 shadow-soft transition-shadow duration-300 hover:shadow-elevated {feature.colSpan}"
				>
					<div
						class="absolute top-8 right-8 text-6xl font-light text-border-medium/30 transition-colors duration-500 group-hover:text-border-medium/60"
						style="font-family: var(--font-heading);"
					>
						0{i + 1}
					</div>
					<h3
						class="mb-3 text-2xl font-light text-primary"
						style="font-family: var(--font-heading);"
					>
						{feature.title}
					</h3>
					<p class="leading-relaxed text-secondary">{feature.desc}</p>
				</div>
			{/each}
		</div>
	</section>

	<!-- Types of Wardrobes: Horizontal/Masonry visual approach -->
	<section class="overflow-hidden bg-white px-6 py-24">
		<div class="mx-auto max-w-7xl">
			<div class="mb-16 flex flex-col items-end justify-between gap-8 lg:flex-row">
				<div class="max-w-2xl">
					<span class="mb-4 block text-sm font-medium tracking-[0.2em] text-accent uppercase"
						>Варианты решений</span
					>
					<h2
						class="text-3xl font-light tracking-wide text-primary lg:text-4xl"
						style="font-family: var(--font-heading);"
					>
						Виды систем
					</h2>
				</div>
			</div>

			<div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
				<!-- Card 1 -->
				<div class="group cursor-pointer">
					<div
						class="relative mb-6 flex aspect-[3/4] items-center justify-center overflow-hidden rounded-2xl bg-[#F0F0F0] transition-all duration-500 group-hover:bg-[#E5E5E5]"
					>
						<div
							class="absolute inset-x-0 bottom-0 h-1/2 bg-gradient-to-t from-primary/10 to-transparent"
						></div>
						<span
							class="relative z-10 text-xs font-medium tracking-[0.2em] text-primary/40 uppercase"
							>Заглушка: Встроенный шкаф</span
						>
					</div>
					<h3
						class="mb-2 text-xl font-light tracking-wide text-primary"
						style="font-family: var(--font-heading);"
					>
						Встроенные шкафы
					</h3>
					<p class="text-sm leading-relaxed text-secondary">
						Монтируются от пола до потолка, скрывая неровности стен и максимально эффективно
						используя ниши
					</p>
				</div>

				<!-- Card 2 -->
				<div class="group cursor-pointer lg:-translate-y-8">
					<div
						class="relative mb-6 flex aspect-[3/4] items-center justify-center overflow-hidden rounded-2xl bg-[#E8E8E8] transition-all duration-500 group-hover:bg-[#DDDDDD]"
					>
						<div
							class="absolute inset-x-0 bottom-0 h-1/2 bg-gradient-to-t from-primary/10 to-transparent"
						></div>
						<span
							class="relative z-10 text-xs font-medium tracking-[0.2em] text-primary/40 uppercase"
							>Заглушка: Корпусный шкаф</span
						>
					</div>
					<h3
						class="mb-2 text-xl font-light tracking-wide text-primary"
						style="font-family: var(--font-heading);"
					>
						Корпусные решения
					</h3>
					<p class="text-sm leading-relaxed text-secondary">
						Самостоятельные модули, которые можно перемещать. Акцентные фасады и витринные
						стеклянные элементы
					</p>
				</div>

				<!-- Card 3 -->
				<div class="group cursor-pointer lg:-translate-y-16">
					<div
						class="relative mb-6 flex aspect-[3/4] items-center justify-center overflow-hidden rounded-2xl bg-[#F0F0F0] transition-all duration-500 group-hover:bg-[#E5E5E5]"
					>
						<div
							class="absolute inset-x-0 bottom-0 h-1/2 bg-gradient-to-t from-primary/10 to-transparent"
						></div>
						<span
							class="relative z-10 text-xs font-medium tracking-[0.2em] text-primary/40 uppercase"
							>Заглушка: Гардеробная</span
						>
					</div>
					<h3
						class="mb-2 text-xl font-light tracking-wide text-primary"
						style="font-family: var(--font-heading);"
					>
						Гардеробные комнаты
					</h3>
					<p class="text-sm leading-relaxed text-secondary">
						Открытые и закрытые модульные системы премиум-класса с умной подсветкой и организаторами
					</p>
				</div>
			</div>
		</div>
	</section>

	<!-- Minimal Footer CTA -->
	<section class="border-t border-border-light bg-surface-warm px-6 py-24">
		<div class="mx-auto max-w-4xl text-center">
			<h2
				class="mb-8 text-3xl font-light tracking-wide text-primary lg:text-5xl"
				style="font-family: var(--font-heading);"
			>
				Закажите расчет стоимости
			</h2>
			<button
				class="group inline-flex cursor-pointer items-center gap-3 border border-primary bg-primary px-8 py-4 text-xs tracking-[0.15em] text-white uppercase transition-all duration-500 hover:bg-transparent hover:text-primary rounded-sm"
				onclick={() => (isShowroomModalOpen = true)}
			>
				Запись в салон
				<svg class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
					<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M14 5l7 7m0 0l-7 7m7-7H3" />
				</svg>
			</button>
		</div>
	</section>
</main>

<Modal bind:showModal={isShowroomModalOpen} title="Запись в салон">
	<ShowroomForm onSuccess={() => (isShowroomModalOpen = false)} />
</Modal>
