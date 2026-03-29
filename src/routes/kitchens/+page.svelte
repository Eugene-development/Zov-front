<script>
	import { fade, fly } from 'svelte/transition';
	import { onMount } from 'svelte';
	import Modal from '$lib/components/Modal.svelte';
	import ShowroomForm from '$lib/components/ShowroomForm.svelte';
	import DesignProjectForm from '$lib/components/DesignProjectForm.svelte';

	let isVisible = $state(false);
	let galleryVisible = $state(false);
	let cycleVisible = $state(false);
	let isShowroomModalOpen = $state(false);
	let isDesignProjectModalOpen = $state(false);

	function viewport(element, callback) {
		const observer = new IntersectionObserver(
			(entries) => {
				entries.forEach((entry) => {
					if (entry.isIntersecting) {
						callback();
						observer.unobserve(element);
					}
				});
			},
			{ threshold: 0.1, rootMargin: '50px' }
		);
		observer.observe(element);
		return {
			destroy() {
				observer.disconnect();
			}
		};
	}

	onMount(() => {
		isVisible = true;
	});
</script>

<svelte:head>
	<title>Кухни | Процесс производства | ЗОВ</title>
	<meta
		name="description"
		content="Полный цикл создания премиальных кухонь ЗОВ: от проектирования технологами до бережной доставки и финальной сборки."
	/>
</svelte:head>

<main class="bg-white">
	<!-- Hero Section -->
	<section
		class="relative flex min-h-[calc(100vh-64px)] lg:min-h-[calc(100vh-120px)] items-center justify-center overflow-hidden bg-primary text-inverse"
	>
		<div class="absolute inset-0 z-0">
			<img
				src="/images/kitchen_assembly.png"
				alt="Премиальные кухни ЗОВ"
				class="h-full w-full object-cover opacity-30 mix-blend-overlay"
			/>
			<div
				class="absolute inset-0 bg-gradient-to-b from-primary/80 via-primary/50 to-primary/95"
			></div>
		</div>
		<div class="relative z-10 mx-auto max-w-screen-xl px-6 xl:px-1 text-center">
			{#if isVisible}
				<h1
					in:fly={{ y: 30, duration: 1000, delay: 100 }}
					class="mb-6 text-4xl font-light tracking-[0.1em] text-white uppercase lg:text-6xl"
					style="font-family: var(--font-heading);"
				>
					Создание вашей идеальной кухни
				</h1>
				<p
					in:fly={{ y: 30, duration: 1000, delay: 300 }}
					class="mx-auto max-w-3xl text-lg leading-relaxed font-light text-white/80 lg:text-xl"
				>
					От детального проектирования до бережной сборки — каждый этап контролируется нашими
					специалистами для достижения безупречного премиального качества
				</p>
				<div in:fly={{ y: 30, duration: 1000, delay: 500 }} class="mt-10">
					<button
						onclick={() => (isDesignProjectModalOpen = true)}
						class="group inline-flex cursor-pointer items-center gap-3 rounded-sm border border-white bg-white px-8 py-4 text-xs tracking-[0.15em] text-primary uppercase transition-all duration-500 hover:bg-transparent hover:text-white"
					>
						Спроектировать кухню
						<svg
							class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="1.5"
								d="M14 5l7 7m0 0l-7 7m7-7H3"
							/>
						</svg>
					</button>
				</div>
			{/if}
		</div>

		<!-- Scroll Indicator -->
		{#if isVisible}
			<div
				class="absolute bottom-10 left-1/2 -translate-x-1/2 animate-fade-in"
				style="animation-delay: 1.5s"
			>
				<div class="flex flex-col items-center gap-2">
					<span class="text-[10px] tracking-[0.3em] text-white/40 uppercase">Листайте</span>
					<div class="h-10 w-px bg-gradient-to-b from-white/40 to-transparent"></div>
				</div>
			</div>
		{/if}
	</section>

	<!-- Gallery Section -->
	<section class="bg-surface-warm px-6 xl:px-1 py-24" use:viewport={() => (galleryVisible = true)}>
		<div class="mx-auto max-w-screen-xl">
			<div class="mb-16 text-center">
				{#if galleryVisible}
					<div in:fly={{ y: 30, duration: 1000 }}>
						<div class="mb-4 text-sm font-medium tracking-[0.2em] text-accent uppercase">
							Галерея
						</div>
						<h2
							class="mb-6 text-3xl font-light tracking-wide text-primary uppercase lg:text-4xl"
							style="font-family: var(--font-heading);"
						>
							Наши гарнитуры
						</h2>
						<p class="mx-auto max-w-2xl text-lg leading-relaxed font-light text-secondary">
							Ознакомьтесь с вариантами решений для вашей кухни. Идеальные пропорции,
							инновационные материалы и европейская фурнитура.
						</p>
					</div>
				{/if}
			</div>

			<div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
				{#each [1, 2, 3, 4, 5, 6] as item, i}
					{#if galleryVisible}
						<div
							in:fly={{ y: 50, duration: 1000, delay: 200 + i * 150 }}
							class="group relative aspect-[4/3] overflow-hidden rounded-2xl bg-white shadow-soft transition-all duration-500 hover:-translate-y-2 hover:shadow-elevated"
						>
							<div class="absolute inset-0 flex flex-col items-center justify-center bg-gradient-to-br from-gray-50 to-gray-200 text-secondary/30 transition-transform duration-700 group-hover:scale-105">
								<svg class="mb-4 h-12 w-12 opacity-50" fill="none" viewBox="0 0 24 24" stroke="currentColor">
									<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
								</svg>
								<span class="text-sm font-medium tracking-[0.2em] uppercase">Проект {item}</span>
							</div>
							<div class="absolute inset-0 bg-primary/0 transition-colors duration-500 group-hover:bg-primary/5"></div>
							<div class="absolute bottom-0 left-0 right-0 translate-y-full bg-white/90 p-6 backdrop-blur-md transition-transform duration-500 group-hover:translate-y-0">
								<h3 class="mb-2 text-lg font-light tracking-wide text-primary" style="font-family: var(--font-heading);">
									Кухонный гарнитур {item}
								</h3>
								<p class="text-sm text-secondary">Премиальная отделка, современный дизайн</p>
							</div>
						</div>
					{/if}
				{/each}
			</div>
		</div>
	</section>

	<!-- Content Sections -->
	<section class="relative px-6 xl:px-1 py-24" use:viewport={() => (cycleVisible = true)}>
		<div class="mx-auto flex max-w-screen-xl flex-col gap-32">
			<!-- Section Header -->
			<div class="mb-16 text-center">
				{#if cycleVisible}
					<div in:fly={{ y: 30, duration: 1000 }}>
						<div class="mb-4 text-sm font-medium tracking-[0.2em] text-accent uppercase">
							Этапы
						</div>
						<h2
							class="mb-6 text-3xl font-light tracking-wide text-primary uppercase lg:text-4xl"
							style="font-family: var(--font-heading);"
						>
							Производственный цикл
						</h2>
						<p class="mx-auto max-w-2xl text-lg leading-relaxed font-light text-secondary">
							Отточенный годами процесс создания премиальной мебели: от прецизионного проектирования
							до профессионального монтажа. Мы гарантируем безупречное качество на каждом этапе.
						</p>
					</div>
				{/if}
			</div>

			<!-- Step 1: Проектирование технологами -->
			<div class="flex flex-col items-center gap-16 lg:flex-row">
				<div class="order-2 lg:order-1 lg:w-1/2">
					<div class="mb-4 text-sm font-medium tracking-[0.2em] text-accent uppercase">
						01. Проектирование
					</div>
					<h2
						class="mb-6 text-3xl font-light tracking-wide text-primary lg:text-4xl"
						style="font-family: var(--font-heading);"
					>
						Проектирование технологами
					</h2>
					<p class="mb-6 leading-relaxed text-secondary">
						Дизайн начинается задолго до производства. Наши инженеры-технологи детально
						прорабатывают проект, учитывая миллиметровые зазоры, нагрузку на фурнитуру, особенности
						материалов и эргономику пространства. Мы применяем новейшее программное обеспечение для
						построения точных 3D-моделей вашей будущей кухни, исключая вероятность ошибок.
					</p>
					<div class="h-px w-24 bg-accent"></div>
				</div>
				<div class="order-1 lg:order-2 lg:w-1/2">
					<div class="relative aspect-[4/3] overflow-hidden rounded-2xl shadow-elevated">
						<img
							src="https://storage.yandexcloud.net/zovtop/foto/technoljergbmeogkmbktgg.jpg"
							alt="Проектирование кухни технологами"
							class="h-full w-full object-cover transition-transform duration-700 hover:scale-105"
						/>
					</div>
				</div>
			</div>

			<!-- Step 2: Производственный процесс -->
			<div class="flex flex-col items-center gap-16 lg:flex-row">
				<div class="lg:w-1/2">
					<div class="relative aspect-[4/3] overflow-hidden rounded-2xl shadow-elevated">
						<img
							src="https://storage.yandexcloud.net/zovtop/foto/proizvodlkfegbmrgbm.jpg"
							alt="Производственный процесс"
							class="h-full w-full object-cover transition-transform duration-700 hover:scale-105"
						/>
					</div>
				</div>
				<div class="lg:w-1/2">
					<div class="mb-4 text-sm font-medium tracking-[0.2em] text-accent uppercase">
						02. Производство
					</div>
					<h2
						class="mb-6 text-3xl font-light tracking-wide text-primary lg:text-4xl"
						style="font-family: var(--font-heading);"
					>
						Работа в наших цехах
					</h2>
					<p class="mb-6 leading-relaxed text-secondary">
						Производство кухонь ЗОВ — это симбиоз передовых роботизированных линий и ручного
						мастерства. Мы используем европейское оборудование сверхвысокой
						точности для распила и кромления, что гарантирует идеальную геометрию фасадов,
						долговечность фурнитуры и высочайшее качество готовых изделий.
					</p>
					<div class="h-px w-24 bg-accent"></div>
				</div>
			</div>

			<!-- Steps 3 & 4: Упаковка & Доставка -->
			<div class="relative grid grid-cols-1 gap-16 py-12 md:grid-cols-2">
				<!-- Decorative background elements -->
				<div
					class="absolute inset-0 -z-10 -mx-6 rounded-3xl bg-surface-warm px-6 xl:px-1 lg:-mx-12 lg:px-6 xl:px-12"
				></div>

				<div class="p-8 lg:p-12">
					<div
						class="mb-4 flex h-12 w-12 items-center justify-center rounded-full bg-white shadow-soft"
					>
						<svg class="h-6 w-6 text-accent" fill="none" viewBox="0 0 24 24" stroke="currentColor">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="1.5"
								d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"
							/>
						</svg>
					</div>
					<div class="mb-4 text-sm font-medium tracking-[0.2em] text-accent uppercase">
						03. Логистика
					</div>
					<h2
						class="mb-6 text-2xl font-light tracking-wide text-primary lg:text-3xl"
						style="font-family: var(--font-heading);"
					>
						Бережная упаковка
					</h2>
					<p class="leading-relaxed text-secondary">
						Каждая деталь вашей будущей кухни проходит многоуровневый контроль качества. Затем
						элементы бережно упаковываются в плотный многослойный картон с защитными профилями. Это
						полностью исключает любые повреждения, царапины и деформации при перемещении.
					</p>
				</div>

				<div class="p-8 lg:p-12">
					<div
						class="mb-4 flex h-12 w-12 items-center justify-center rounded-full bg-white shadow-soft"
					>
						<svg class="h-6 w-6 text-accent" fill="none" viewBox="0 0 24 24" stroke="currentColor">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="1.5"
								d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"
							/>
						</svg>
					</div>
					<div class="mb-4 text-sm font-medium tracking-[0.2em] text-accent uppercase">
						04. Транспортировка
					</div>
					<h2
						class="mb-6 text-2xl font-light tracking-wide text-primary lg:text-3xl"
						style="font-family: var(--font-heading);"
					>
						Безопасная доставка
					</h2>
					<p class="leading-relaxed text-secondary">
						Доставка осуществляется нашим собственным автопарком, оборудованным специальными
						пневматическими креплениями для перевозки элитной мебели. Наши экипажи аккуратно
						поднимают изделия на ваш этаж, соблюдая чистоту и бережное отношение к ремонту.
					</p>
				</div>
			</div>

			<!-- Step 5: Сборка -->
			<div class="flex flex-col items-center gap-16 lg:flex-row">
				<div class="order-2 lg:order-1 lg:w-1/2">
					<div class="mb-4 text-sm font-medium tracking-[0.2em] text-accent uppercase">
						05. Финал
					</div>
					<h2
						class="mb-6 text-3xl font-light tracking-wide text-primary lg:text-4xl"
						style="font-family: var(--font-heading);"
					>
						Профессиональная сборка
					</h2>
					<p class="mb-6 leading-relaxed text-secondary">
						Сборкой кухонь занимаются собственные бригады сертифицированных специалистов ЗОВ. Они
						монтируют корпуса, выставляют идеальные зазоры фасадов, подключают встраиваемую технику
						и интегрируют освещение. В результате вы получаете кухню мечты премиум-класса, полностью
						готовую к вашему первому кулинарному шедевру.
					</p>
					<div class="h-px w-24 bg-accent"></div>
				</div>
				<div class="order-1 lg:order-2 lg:w-1/2">
					<div class="relative aspect-[4/3] overflow-hidden rounded-2xl shadow-elevated">
						<img
							src="/images/kitchen_assembly.png"
							alt="Сборка кухни"
							class="h-full w-full object-cover transition-transform duration-700 hover:scale-105"
						/>
					</div>
				</div>
			</div>
		</div>
	</section>

	<!-- Kitchen Variations Section -->
	<section class="bg-surface-warm px-6 xl:px-1 py-24">
		<div class="mx-auto max-w-screen-xl">
			<div class="mb-16 text-center">
				<h2
					class="mb-6 text-3xl font-light tracking-wide text-primary uppercase lg:text-4xl"
					style="font-family: var(--font-heading);"
				>
					Варианты стилистических решений
				</h2>
				<p class="mx-auto max-w-2xl text-lg leading-relaxed font-light text-secondary">
					Мы адаптируем индивидуальный проект под любой стиль. Выберите то, что идеально дополнит
					ваш интерьер. Каждая кухня от ЗОВ уникальна.
				</p>
			</div>

			<div class="grid grid-cols-1 gap-8 md:grid-cols-3">
				<!-- Option 1 -->
				<div
					class="group overflow-hidden rounded-2xl bg-white shadow-soft transition-all duration-300 hover:-translate-y-2 hover:shadow-elevated"
				>
					<div class="aspect-[4/3] w-full overflow-hidden">
						<img
							src="/images/style-modern.png"
							alt="Современный стиль кухни"
							class="h-full w-full object-cover transition-transform duration-700 group-hover:scale-105"
						/>
					</div>
					<div class="p-8">
						<h3
							class="mb-3 text-xl font-light tracking-wide text-primary"
							style="font-family: var(--font-heading);"
						>
							Современный стиль
						</h3>
						<p class="text-sm leading-relaxed text-secondary">
							Минимализм в каждой детали. Гладкие матовые фасады, скрытая фурнитура, отсутствие
							лишних визуальных шумов. Идеально для функционального и чистого пространства.
						</p>
					</div>
				</div>

				<!-- Option 2 -->
				<div
					class="group overflow-hidden rounded-2xl bg-white shadow-soft transition-all duration-300 hover:-translate-y-2 hover:shadow-elevated"
				>
					<div class="aspect-[4/3] w-full overflow-hidden">
						<img
							src="/images/style-neoclassic.png"
							alt="Стиль неоклассика"
							class="h-full w-full object-cover transition-transform duration-700 group-hover:scale-105"
						/>
					</div>
					<div class="p-8">
						<h3
							class="mb-3 text-xl font-light tracking-wide text-primary"
							style="font-family: var(--font-heading);"
						>
							Неоклассика
						</h3>
						<p class="text-sm leading-relaxed text-secondary">
							Утонченное сочетание традиций и современных тенденций. Изящная неглубокая фрезеровка
							фасадов, пастельная цветовая палитра и премиальные, приятные на ощупь материалы.
						</p>
					</div>
				</div>

				<!-- Option 3 -->
				<div
					class="group overflow-hidden rounded-2xl bg-white shadow-soft transition-all duration-300 hover:-translate-y-2 hover:shadow-elevated"
				>
					<div class="aspect-[4/3] w-full overflow-hidden">
						<img
							src="/images/style-loft.png"
							alt="Стиль лофт"
							class="h-full w-full object-cover transition-transform duration-700 group-hover:scale-105"
						/>
					</div>
					<div class="p-8">
						<h3
							class="mb-3 text-xl font-light tracking-wide text-primary"
							style="font-family: var(--font-heading);"
						>
							Лофт
						</h3>
						<p class="text-sm leading-relaxed text-secondary">
							Выразительная фактура натурального дерева, бетона и металла. Брутальные формы,
							индустриальный шик и максимальный акцент на естественные, природные покрытия.
						</p>
					</div>
				</div>
			</div>
		</div>
	</section>

	<!-- Call to Action -->
	<section class="bg-primary px-6 xl:px-1 py-24 text-center text-white">
		<h2
			class="mb-8 text-3xl font-light tracking-wide uppercase lg:text-4xl"
			style="font-family: var(--font-heading);"
		>
			Хотите заказать кухню?
		</h2>
		<p class="mx-auto mb-10 max-w-2xl text-lg font-light text-white/70">
			Запишитесь в наши салоны для бесплатной консультации с дизайнером, знакомства с материалами и
			расчета стоимости вашего проекта.
		</p>
		<button
			class="inline-flex cursor-pointer items-center gap-2 rounded-sm border border-accent bg-accent px-8 py-4 text-sm tracking-wider text-white transition-all duration-300 hover:bg-transparent hover:text-accent"
			onclick={() => (isShowroomModalOpen = true)}
		>
			Записаться в салон
			<svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="1.5"
					d="M14 5l7 7m0 0l-7 7m7-7H3"
				/>
			</svg>
		</button>
	</section>
</main>

<Modal bind:showModal={isShowroomModalOpen} title="Запись в салон">
	<ShowroomForm onSuccess={() => (isShowroomModalOpen = false)} />
</Modal>

<Modal bind:showModal={isDesignProjectModalOpen} title="Заказ дизайн-проекта">
	<DesignProjectForm onSuccess={() => (isDesignProjectModalOpen = false)} />
</Modal>
