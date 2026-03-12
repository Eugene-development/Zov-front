<script>
	import { onMount } from 'svelte';

	let heroVisible = $state(false);
	let sections = $state({});

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

		document.querySelectorAll('[data-animate]').forEach((el) => {
			observer.observe(el);
		});

		return () => observer.disconnect();
	});

	const brands = [
		{
			id: 'blum',
			name: 'Blum',
			origin: 'Австрия',
			description:
				'Австрийская компания Blum — признанный лидер в мире фурнитуры. Это синоним безупречного движения, долговечности и инноваций. Механизмы Blum рассчитаны на срок службы всей мебели и даже больше, обеспечивая плавность закрывания и комфорт в каждом движении.',
			image: '/images/blum_hardware.png',
			features: [
				'Системы петель CLIP top BLUMOTION',
				'Подъемные механизмы AVENTOS',
				'Премиальные системы выдвижения LEGRABOX',
				'Повышенная гарантия на механизмы'
			],
			reverse: false
		},
		{
			id: 'hettich',
			name: 'Hettich',
			origin: 'Германия',
			description:
				'Немецкое качество Hettich устанавливает стандарты во всем мире. Интеллектуальные технологии сочетаются с лаконичным дизайном. Hettich обеспечивает максимальную стабильность для самых широких и тяжелых фасадов, делая вашу мебель надежной и совершенной.',
			image: '/images/hettich_hardware.png',
			features: [
				'Системы выдвижных ящиков ArciTech',
				'Инновационные петли Sensys',
				'Скрытые направляющие Quadro',
				'Высочайшая немецкая надежность'
			],
			reverse: true
		},
		{
			id: 'gtv',
			name: 'GTV',
			origin: 'Польша',
			description:
				'Динамично развивающийся европейский бренд GTV предлагает современные решения для любой мебели. Это оптимальное сочетание высокого качества, премиального комфорта, новейших трендов в дизайне и ценовой доступности.',
			image: '/images/gtv_hardware.png',
			features: [
				'Ультратонкие ящики Axis Pro',
				'Системы скрытого монтажа Modern SLIDE PRO',
				'Петли с доводчиком SILENTO PRO',
				'Оптимальное соотношение цена/качество'
			],
			reverse: false
		}
	];
</script>

<svelte:head>
	<title>Мебельная фурнитура | Blum, Hettich, GTV | ЗОВ</title>
	<meta
		name="description"
		content="Надежная и долговечная мебельная фурнитура от ведущих мировых производителей: Blum, Hettich, GTV. Безупречный комфорт для вашей мебели ЗОВ."
	/>
</svelte:head>

<!-- ==================== HERO SECTION ==================== -->
<section class="relative min-h-[90vh] overflow-hidden bg-surface" id="hero">
	<!-- Background Image with Dark Overlay -->
	<div class="absolute inset-0">
		<img
			src="/images/furniture_hero.png"
			alt="Премиальная мебельная фурнитура"
			class="h-full w-full object-cover transition-transform duration-[2.5s]"
			class:scale-105={heroVisible}
		/>
		<div
			class="absolute inset-0 bg-gradient-to-r from-primary/95 via-primary/70 to-primary/40"
		></div>
	</div>

	<!-- Content -->
	<div class="relative z-10 flex min-h-[90vh] items-center">
		<div class="mx-auto w-full max-w-7xl px-6">
			<div class="max-w-2xl">
				<!-- Label -->
				<div
					class="mb-6 opacity-0"
					class:animate-fade-up={heroVisible}
					style="animation-delay: 0.3s"
				>
					<span
						class="inline-flex items-center gap-2 border border-white/20 bg-white/5 px-4 py-2 text-[11px] tracking-[0.25em] text-white/70 uppercase backdrop-blur-sm"
					>
						Функциональность
					</span>
				</div>

				<!-- Heading -->
				<h1
					class="text-5xl leading-[1.1] font-light text-white opacity-0 md:text-6xl lg:text-7xl"
					style="font-family: var(--font-heading); animation-delay: 0.5s"
					class:animate-fade-up={heroVisible}
				>
					Безупречное
					<br />
					движение
				</h1>

				<!-- Description -->
				<p
					class="mt-8 max-w-xl text-base leading-relaxed text-white/70 opacity-0 md:text-lg"
					class:animate-fade-up={heroVisible}
					style="animation-delay: 0.7s"
				>
					Мебель премиум-класса требует фурнитуры соответствующего уровня. Мы предлагаем решения от
					ведущих европейских брендов, которые сделают каждое движение фасада или ящика плавным и
					комфортным.
				</p>

				<div
					class="mt-10 opacity-0"
					class:animate-fade-up={heroVisible}
					style="animation-delay: 0.9s"
				>
					<a
						href="#intro-section"
						class="group inline-flex cursor-pointer items-center gap-3 border border-secondary bg-secondary px-8 py-4 text-xs tracking-[0.15em] text-white uppercase transition-all duration-500 hover:bg-transparent"
					>
						Узнать больше
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

<!-- ==================== INTRO SECTION ==================== -->
<section
	class="relative scroll-mt-20 bg-white py-section-sm lg:scroll-mt-24 lg:py-section"
	id="intro-section"
	data-animate
>
	<div class="mx-auto max-w-7xl px-6 text-center">
		<div class="opacity-0" class:animate-fade-up={sections['intro-section']}>
			<span class="text-[11px] tracking-[0.3em] text-secondary uppercase">Качество в деталях</span>
			<h2
				class="mx-auto mt-6 max-w-3xl text-3xl leading-snug font-light text-primary lg:text-5xl"
				style="font-family: var(--font-heading);"
			>
				Надежность, которую вы <span class="text-secondary">чувствуете</span> каждый день
			</h2>
			<p class="mx-auto mt-8 max-w-2xl text-base leading-relaxed text-text-secondary">
				Фурнитура — это невидимое сердце любой мебели. От нее зависит, насколько плавно будут
				открываться дверцы, как тихо будут закрываться ящики и сколько лет мебель прослужит без
				единого скрипа. Мы подобрали для вас лучшее оборудование от мировых лидеров мебельной
				фурнитуры.
			</p>
		</div>
	</div>
</section>

<!-- ==================== BRANDS SECTION ==================== -->
<section class="relative bg-surface-warm pb-section-sm lg:pb-section">
	<div class="mx-auto max-w-7xl px-6 pt-20">
		<div class="flex flex-col gap-24 lg:gap-32">
			{#each brands as brand, i (brand.id)}
				<div
					class="grid items-center gap-12 lg:grid-cols-2 lg:gap-20"
					id={`brand-${brand.id}`}
					data-animate
				>
					<!-- Content Box -->
					<div
						class="flex flex-col justify-center opacity-0 {brand.reverse ? 'lg:order-last' : ''}"
						class:animate-fade-up={sections[`brand-${brand.id}`]}
						style="animation-delay: 0.2s"
					>
						<span class="text-[11px] tracking-[0.3em] text-secondary uppercase">{brand.origin}</span
						>
						<h3
							class="mt-3 text-4xl font-light tracking-wide text-primary lg:text-6xl"
							style="font-family: var(--font-heading);"
						>
							{brand.name}
						</h3>
						<div class="bg-border-strong mt-6 mb-8 h-px w-12"></div>
						<p class="text-base leading-relaxed text-text-secondary">
							{brand.description}
						</p>
						<ul class="mt-8 flex flex-col gap-5">
							{#each brand.features as feature}
								<li class="flex items-start gap-4">
									<div
										class="mt-1.5 flex h-3 w-3 flex-shrink-0 items-center justify-center border border-secondary"
									>
										<div class="h-1 w-1 bg-secondary"></div>
									</div>
									<span class="text-sm text-text-primary">{feature}</span>
								</li>
							{/each}
						</ul>
					</div>

					<!-- Image Box -->
					<div
						class="relative aspect-[4/3] overflow-hidden opacity-0 lg:aspect-square"
						class:animate-fade-up={sections[`brand-${brand.id}`]}
						style="animation-delay: 0.4s"
					>
						<img
							src={brand.image}
							alt={`Фурнитура ${brand.name}`}
							class="h-full w-full object-cover transition-transform duration-700 hover:scale-105"
						/>
						<div
							class="pointer-events-none absolute inset-0 border-[0.5rem] border-surface-warm/20"
						></div>
					</div>
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- ==================== CTA SECTION ==================== -->
<section
	class="relative overflow-hidden bg-primary py-section-sm lg:py-section"
	id="cta-section"
	data-animate
>
	<!-- Decorative Background -->
	<div class="absolute top-0 left-0 h-40 w-40 border border-white/5 opacity-50"></div>
	<div class="absolute right-0 bottom-0 h-64 w-64 border border-white/5 opacity-50"></div>

	<div class="relative mx-auto max-w-7xl px-6 text-center">
		<div class="opacity-0" class:animate-fade-up={sections['cta-section']}>
			<span class="text-[11px] tracking-[0.3em] text-accent uppercase">консультация</span>
			<h2
				class="mx-auto mt-6 max-w-2xl text-3xl font-light text-white lg:text-5xl"
				style="font-family: var(--font-heading);"
			>
				Поможем выбрать <span class="text-accent-light">лучшую систему</span> для вашей мебели
			</h2>
			<p class="mx-auto mt-6 max-w-xl text-sm leading-relaxed text-white/60 lg:text-base">
				Наши дизайнеры подберут фурнитуру, которая идеально подойдет под ваши потребности,
				дизайн-проект и бюджет.
			</p>

			<div class="mt-10 flex flex-wrap items-center justify-center gap-4">
				<a
					href="/showrooms"
					class="group inline-flex items-center gap-3 border border-accent bg-accent px-8 py-4 text-xs tracking-[0.15em] text-primary uppercase transition-all duration-500 hover:border-accent-light hover:bg-accent-light"
				>
					Записаться в салон
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
				</a>
			</div>
		</div>
	</div>
</section>
