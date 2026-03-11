<script lang="ts">
	import { fade } from 'svelte/transition';

	// Data for styles
	const styles = [
		{
			id: 'modern',
			name: 'Современный',
			description:
				'Чистые линии, минимализм, интегрированная техника и матовые текстуры для создания идеального пространства.',
			image: '/images/style-modern.png',
			tags: ['Минимализм', 'Hi-Tech', 'Матовость']
		},
		{
			id: 'classic',
			name: 'Классика',
			description:
				'Традиционные формы, резные фасады, обилие дерева и теплые оттенки для уюта и респектабельности.',
			image: '/images/style-classic.png',
			tags: ['Дерево', 'Резьба', 'Патина']
		},
		{
			id: 'loft',
			name: 'Лофт',
			description:
				'Индустриальный шик: бетон, кирпич, металл и брутальные формы, создающие стильное современное пространство.',
			image: '/images/style-loft.png',
			tags: ['Бетон', 'Металл', 'Брутальность']
		},
		{
			id: 'neoclassic',
			name: 'Неоклассика',
			description:
				'Изящное сочетание традиционных элементов с современными материалами и светлыми тонами.',
			image: '/images/style-neoclassic.png',
			tags: ['Изящность', 'Мрамор', 'Светлые тона']
		},
		{
			id: 'minimalist',
			name: 'Скандинавский',
			description:
				'Максимум света и пространства, натуральные материалы, светлое дерево и функциональный лаконичный дизайн.',
			image: '/images/style-minimalist.png',
			tags: ['Свет', 'Уют', 'Функциональность']
		},
		{
			id: 'provence',
			name: 'Прованс',
			description:
				'Французский кантри с пастельными тонами, винтажной фурнитурой и домашним теплом.',
			image: '/images/style-provence.png',
			tags: ['Кантри', 'Винтаж', 'Уют']
		}
	];
</script>

<svelte:head>
	<title>Стили кухонь | ZOV</title>
	<meta
		name="description"
		content="Выберите идеальный стиль для вашей новой кухни ZOV. От современной минималистики до элегантной классики."
	/>
</svelte:head>

<div class="min-h-screen bg-primary text-white">
	<!-- Hero Section -->
	<section class="relative flex h-[60vh] items-center justify-center overflow-hidden md:h-[70vh]">
		<div class="absolute inset-0 bg-[url('/images/style-neoclassic.png')] bg-cover bg-center"></div>
		<div class="absolute inset-0 bg-gradient-to-b from-black/80 via-black/60 to-primary"></div>

		<div
			class="relative z-10 mx-auto max-w-4xl px-4 text-center"
			in:fade={{ duration: 1000, delay: 200 }}
		>
			<h1 class="mb-6 text-5xl font-bold tracking-tight md:text-7xl">
				<span class="block bg-gradient-to-r from-white to-white/70 bg-clip-text text-transparent">
					Стили кухонь
				</span>
			</h1>
			<p class="mx-auto max-w-2xl text-xl leading-relaxed font-light text-white/80 md:text-2xl">
				Откройте для себя наше портфолио и найдите вдохновение для создания кухонного гарнитура,
				отражающего ваш вкус и индивидуальный стиль жизни.
			</p>
		</div>
	</section>

	<!-- Styles Grid -->
	<section class="mx-auto max-w-7xl px-4 py-24 sm:px-6 lg:px-8">
		<div class="grid grid-cols-1 gap-8 md:grid-cols-2 md:gap-12 lg:grid-cols-3">
			{#each styles as style}
				<div
					class="group relative aspect-[4/5] cursor-pointer overflow-hidden rounded-2xl bg-neutral-900 shadow-xl transition-all duration-500 hover:-translate-y-2 hover:shadow-2xl hover:shadow-white/10"
				>
					<!-- Background Image with Zoom on Hover -->
					<img
						src={style.image}
						alt={style.name}
						class="absolute inset-0 h-full w-full object-cover transition-transform duration-700 group-hover:scale-110"
					/>

					<!-- Gradient Overlay -->
					<div
						class="absolute inset-0 bg-gradient-to-t from-black/95 via-black/50 to-transparent opacity-80 transition-opacity duration-500 group-hover:opacity-100"
					></div>

					<!-- Additional Dark Overlay for readable text on hover -->
					<div
						class="absolute inset-0 bg-black/40 opacity-0 mix-blend-multiply transition-opacity duration-500 group-hover:opacity-100"
					></div>

					<!-- Content Content -->
					<div
						class="absolute inset-x-0 bottom-0 flex translate-y-8 flex-col justify-end p-8 transition-transform duration-500 ease-out group-hover:translate-y-0"
					>
						<h2 class="mb-3 text-3xl font-bold text-white">
							{style.name}
						</h2>
						<p
							class="mb-6 line-clamp-3 leading-relaxed text-white/70 opacity-0 transition-opacity delay-100 duration-500 group-hover:opacity-100"
						>
							{style.description}
						</p>

						<div
							class="flex flex-wrap gap-2 opacity-0 transition-opacity delay-200 duration-500 group-hover:opacity-100"
						>
							{#each style.tags as tag}
								<span
									class="rounded-full border border-white/10 bg-white/10 px-3 py-1 text-xs font-medium text-white/90 backdrop-blur-md"
								>
									{tag}
								</span>
							{/each}
						</div>

						<!-- Interactive Arrow -->
						<!-- <div
							class="absolute right-8 bottom-8 translate-x-4 opacity-0 transition-all delay-300 duration-500 group-hover:translate-x-0 group-hover:opacity-100"
						>
							<div
								class="flex h-10 w-10 items-center justify-center rounded-full bg-white text-black"
							>
								<svg
									xmlns="http://www.w3.org/2000/svg"
									class="h-5 w-5"
									viewBox="0 0 20 20"
									fill="currentColor"
								>
									<path
										fill-rule="evenodd"
										d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z"
										clip-rule="evenodd"
									/>
								</svg>
							</div>
						</div> -->
					</div>
				</div>
			{/each}
		</div>
	</section>

	<!-- CTA Section -->
	<section class="relative overflow-hidden py-24">
		<div class="absolute inset-0 bg-neutral-900"></div>
		<!-- Decorative glow -->
		<div
			class="pointer-events-none absolute top-1/2 left-1/2 h-[800px] w-[800px] -translate-x-1/2 -translate-y-1/2 rounded-full bg-white/5 blur-[120px]"
		></div>

		<div class="relative z-10 mx-auto max-w-4xl px-4 text-center">
			<h2 class="mb-6 text-4xl font-bold text-white md:text-5xl">Нашли идеальный стиль?</h2>
			<p class="mx-auto mb-10 max-w-2xl text-xl font-light text-white/70">
				Запишитесь на бесплатную консультацию с профессиональным дизайнером в салоне. Мы поможем
				адаптировать любой стиль под размеры вашей кухни и ваши потребности.
			</p>

			<button
				class="group relative overflow-hidden rounded-full bg-white px-8 py-4 text-lg font-medium text-black shadow-[0_0_40px_rgba(255,255,255,0.2)] transition-all hover:scale-105 active:scale-95"
			>
				<span class="relative z-10 flex items-center gap-2">
					Запись в салон ЗОВ
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-5 w-5 transition-transform group-hover:translate-x-1"
						viewBox="0 0 20 20"
						fill="currentColor"
					>
						<path
							fill-rule="evenodd"
							d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z"
							clip-rule="evenodd"
						/>
					</svg>
				</span>
				<div
					class="absolute inset-0 bg-gradient-to-r from-white via-neutral-200 to-white opacity-0 transition-opacity group-hover:opacity-100"
				></div>
			</button>
		</div>
	</section>
</div>
