import Carousel from 'react-bootstrap/Carousel';
import { useEffect, useState } from 'react';
import CarouselImage from './CarouselImage';
import api from '../api/helpers/Api';
import Path from '../paths';

export default function Home() {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    api.get(Path.CATEGORIES)
    .then(response => response.data)
      .then(state => setCategories(state));
  }, []);

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