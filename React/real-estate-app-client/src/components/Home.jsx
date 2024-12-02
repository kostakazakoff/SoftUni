import Carousel from 'react-bootstrap/Carousel';
import { useContext } from 'react';
import CarouselImage from './CarouselImage';
import CategoriesContext from '../api/contexts/CategoriesContext';

export default function Home() {
  const categories = useContext(CategoriesContext);

  return (
    <Carousel style={{ textAlign: 'center' }}>
      {categories.map(category => (
        <Carousel.Item key={category.id}>
          <CarouselImage text="Rent" />
          <Carousel.Caption>
            <h3>{category.name}</h3>
          </Carousel.Caption>
        </Carousel.Item >
      ))}
    </Carousel>
  );
}