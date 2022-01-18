package kira.niveaux;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;
import org.springframework.data.rest.webmvc.RepositoryRestController;

@RepositoryRestResource(collectionResourceRel = "niveaux", path = "niveaux")
public interface NiveauxRepository extends MongoRepository<Niveaux, String> {
}
